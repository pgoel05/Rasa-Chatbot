from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from twisted.web.static import File
from twisted.web.resource import NoResource
from klein import Klein
from collections import defaultdict
from datetime import datetime
import json
import logging
from uuid import uuid4
from rasa_core.interpreter import RasaNLUInterpreter
import requests
from requests.auth import HTTPBasicAuth

from rasa_nlu.server import check_cors
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.channel import InputChannel, OutputChannel
from rasa_core.events import SlotSet

json_data = open("message_store.json").read()
data = json.loads(json_data)
k = list(data.keys())[-1]
v = list(data.values())[-1]
kv = {k:v}
big_data = [[k],kv]
new_data = json.dumps(big_data)
api_endpoint = "https://f84cc1353869.ap1.hana.ondemand.com/ValeurHR/VHRHRM/ChatBot/WebContent/backendArtifacts/xsjs/InsertBotData.xsjs"
requests.post(url = api_endpoint,data = new_data, auth=HTTPBasicAuth("Val_Dev1", "superAdminDev@1234"))

logger = logging.getLogger()

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')

class FileMessageStore:

    DEFAULT_FILENAME = "message_store.json"

    def __init__(self, filename = DEFAULT_FILENAME):
        self._store = defaultdict(list)
        self._filename = filename
        try:
            for k, v in json.load(open(self._filename, "r")).items():
                self._store[k] = v
        except IOError:
            pass

    def log(self, cid, username, message, uuid=None):
        if uuid is None:
            uuid = str(uuid4())
        self._store[cid].append(
            {
                "time": datetime.utcnow().isoformat(),
                "username": username,
                "message": message,
                "uuid": uuid,
            }
        )
        self.save()

    def clear(self, cid):
        self._store[cid] = []
        self.save()

    def save(self):
        json.dump(self._store, open(self._filename, "w"))

    def __getitem__(self, key):
        return self._store[key]



class BotServerOutputChannel(OutputChannel):
    def __init__(self, message_store):
        self.message_store = message_store

    def send_text_message(self, recipient_id, message):
        self.message_store.log(recipient_id, "bot", {"type": "text", "text": message})

    def send_text_with_buttons(self, recipient_id, message, buttons, **kwargs):
        # type: (Text, Text, List[Dict[Text, Any]], **Any) -> None
        """Sends buttons to the output.
        Default implementation will just post the buttons as a string."""

        self.send_text_message(recipient_id, message)
        self.message_store.log(
            recipient_id, "bot", {"type": "button", "buttons": buttons}
        )

    def send_image_url(self, recipient_id, image_url):
        # type: (Text, Text) -> None
        """Sends an image. Default will just post the url as a string."""

        self.message_store.log(
            recipient_id, "bot", {"type": "image", "image": image_url}
        )

##	def send_link_url(self, recipient_id, link_url):
##        # type: (Text, Text) -> None
##        """Sends an image. Default will just post the url as a string."""
##
##        self.message_store.log(
##            recipient_id, "bot", {"type": "link", "links": link_url}
##        )

class BotServerInputChannel(InputChannel):

    app = Klein()

    def __init__(
        self, agent, port=2018, static_files=None, message_store=FileMessageStore()
    ):
        logging.basicConfig(level="DEBUG")
        logging.captureWarnings(True)
        self.message_store = message_store
        self.static_files = static_files
        self.on_message = lambda x: None
        self.cors_origins = [u'*']
        self.agent = agent
        self.port = port

    @app.route("/conversations/<cid>/log", methods=["GET"])
    @check_cors
    def show_log(self, request, cid):
        request.setHeader("Content-Type", "application/json")
        return json.dumps(self.message_store[cid])

    @app.route("/conversations/<cid>/say", methods=["GET"])
    @check_cors
    def say(self, request, cid):
        message, = request.args.get(b"message", [])
        _payload = request.args.get(b"payload", [])
        _display_name = request.args.get(b"display_name", [])
        _uuid = request.args.get(b"uuid", [])
        logger.info(message)

        if len(_display_name) > 0:
            display_name, = _display_name
            tracker = self.agent.tracker_store.get_or_create_tracker(cid)
            if (
                "display_name" in tracker.current_slot_values()
                and tracker.get_slot("display_name") != display_name
            ):
                tracker.update(SlotSet("display_name", display_name.decode("utf-8")))
                self.agent.tracker_store.save(tracker)

        if message == "_restart":
            self.message_store.clear(cid)
        else:
            if len(_uuid) > 0:
                self.message_store.log(
                    cid,
                    cid,
                    {"type": "text", "text": message.decode("utf-8")},
                    _uuid[0].decode("utf-8"),
                )
            else:
                self.message_store.log(
                    cid, cid, {"type": "text", "text": message.decode("utf-8")}
                )

        if len(_payload) > 0:
            self.on_message(
                UserMessage(
                    _payload[0].decode("utf-8"),
                    output_channel=BotServerOutputChannel(self.message_store),
                    sender_id=cid,
                )
            )
        else:
            self.on_message(
                UserMessage(
                    message.decode("utf-8"),
                    output_channel=BotServerOutputChannel(self.message_store),
                    sender_id=cid,
                )
            )

    @app.route("/health", methods=["GET"])
    def health(self, request):
        return "healthy"

    @app.route("/", branch=True, methods=["GET"])
    @check_cors
    def static(self, request):
        if self.static_files is None:
            return NoResource()
        else:
            return File(self.static_files)

    def start(self, on_message):
        self.on_message = on_message
        logger.info("Started http server on port %d" % self.port)
        self.app.run("0.0.0.0", self.port)

    def start_async_listening(self, message_queue):
        self.start(message_queue.enqueue)

    def start_sync_listening(self, message_handler):
        self.start(message_handler)
