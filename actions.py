from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset

import requests
from requests.auth import HTTPBasicAuth
import json

class ActionPause(Action):

    def name(self):
        return "Action_Pause"

    def run(self, dispatcher, tracker, domain):

        return [ConversationPaused()]

class ActionDateTime(Action):
	def name(self):
		return 'Action_Date_Time'

	def run(self, dispatcher, tracker, domain):
		import datetime
		date = tracker.get_slot('date')
		dat = datetime.datetime.now().strftime("%d/%m/%Y")

		response = """The date today is {}.""".format(dat)

		dispatcher.utter_message(response)
		return [SlotSet('date',dat)]



class ActionYesNo(Action):
	def name(self):
		return 'Action_Yes_No'

	def run(self, dispatcher, tracker, domain):
		user_yesno = tracker.get_slot('yesorno')
		if user_yesno == 'yes':
			response = 'Alright. I am going to hand over the conversation to a live agent.'
		elif user_yesno == 'no':
			response = 'Go ahead. I am ready to help'

		dispatcher.utter_message(response)
		return [SlotSet('yesorno',user_yesno)]
###################################################employee portal##############################################################

class Actiondepartment(Action):
	def name(self):
		return 'Action_Department'

	def run(self, dispatcher, tracker, domain):
		dept = tracker.get_slot('dept')
		if dept == "department_master":
			response = "To add, edit, activate or deactivate organization departments, go to Employee Portal > Department or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/DepartmentMaster/WebContent/index.html."
		elif dept == "sub_department_master":
			response = "To add, edit, activate or deactivate organization sub-departments, go to Employee Portal > Sub-Department or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/SubDepartmentMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('dept',dept)]
##department


class ActionOrganization(Action):
	def name(self):
		return 'Action_Organization'

	def run(self, dispatcher, tracker, domain):
		org = tracker.get_slot('org')
		if org == "organization_master":
			response = "To add, edit, activate or deactivate organization departments, go to Employee Portal > Department or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/OrganizationMaster/WebContent/index.html."
		elif org == "organization_structure_maintainance":
			response = "To create or edit organization structure, go to Employee Portal > Org Structure Maintainance or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeRelationV1/index.html."
		elif org == "organization_type_master":
			response = "To view organization type master, go to Relationship Management > Organization Type Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/OrganisationTypeMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('org',org)]

##organization

class ActionRnr(Action):
	def name(self):
		return 'Action_Rnr'

	def run(self, dispatcher, tracker, domain):
		rnr = tracker.get_slot('rnr')
		if rnr == "rnr_details":
			response = "To add or modify RNR details, go to Employee Portal > Rewards and Recognitions Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RNRDetails/WebContent/index.html."
		elif rnr == "rnr_category":
			response = "To add or modify RNR categories, go to Employee Portal > Rewards and Recognitions Category or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeRewardsRecognizations/WebContent/index.html."
		elif rnr == "rnr_sub_category":
			response = "To add or modify RNR Sub-categories, go to Employee Portal > Rewards and Recognitions Sub-Category or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RewardsRecognizationSubCategory/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('rnr',rnr)]

##rnrewards

class ActionAsset(Action):
	def name(self):
		return 'Action_Asset'

	def run(self, dispatcher, tracker, domain):
		ass = tracker.get_slot('ass')
		if ass == "employee_asset_details":
			response = "To add edit, activate or deactivate assets available for allocation, go to Employee Portal > Employee Asset Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeAssetDetails/WebContent/index.html."
		elif ass == "asset_sub_category":
			response = "To add edit, activate or deactivate asset sub-categories, go to Employee Portal > Asset Sub-Category or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/AssetSubCategoryMaster/WebContent/index.html."
		elif ass == "asset_category":
			response = "To add edit, activate or deactivate asset categories, go to Employee Portal > Asset Category or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/AssetCategoryMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('ass',ass)]

##assets

class ActionReimbursement(Action):
	def name(self):
		return 'Action_Reimbursement'

	def run(self, dispatcher, tracker, domain):
		reimb = tracker.get_slot('reimb')
		if reimb == "reimbursement_request":
			response = "To create or view a reimbursement request, go to Employee Portal > Reimbursement Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeExpense/WebContent/index.html."
		elif reimb == "reimbursement_approval":
			response = "To approve a reimbursement request, go to Employee Portal > Reimbursement Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeExpenseApproval/WebContent/index.html."
		elif reimb == "reimbursement_category_master":
			response = "To create or view a reimbursement category, go to Employee Portal > Reimbursement Category Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/ReimbursementCategoryMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('reimb',reimb)]

##reimbursement

class ActionLang(Action):
	def name(self):
		return 'Action_Lang'

	def run(self, dispatcher, tracker, domain):
		lang = tracker.get_slot('lang')
		if lang == "language_master":
			response = "To add, edit, delete languages as per your operation, go to Employee Portal > Language Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/LanguageMaster/WebContent/index.html."
		elif lang == "language_details":
		    response = "To add, edit, activate or deactivate organization language list, go to Employee Portal > Language Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/LanguageDetails/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('lang',lang)]

##language

class ActionAnn(Action):
	def name(self):
		return 'Action_Ann'

	def run(self, dispatcher, tracker, domain):
		ann = tracker.get_slot('ann')
		if ann == "org_ann":
			response = "To create or edit organization announcements, go to Employee Portal > Organization Announcements or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/OrganizationUpdateDetails/WebContent/index.html."
		elif ann == "org_ann_type":
			response = "To create or edit organization announcements types, go to Employee Portal > Organization Announcement Types or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/OrgUpdateMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('ann',ann)]

##announcements

class ActionPosition(Action):
	def name(self):
		return 'Action_Position'

	def run(self, dispatcher, tracker, domain):
		pos = tracker.get_slot('pos')
		if pos == "position":
			response = "To add, edit or delete position names, go to Employee Portal > Position or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/PositionMaster/index.html."
		elif pos == "my_profile":
			response = "To view your basic details, go to My Profile > Employee Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeMaster/WebContent/index.html#/Details/EmployeeList(50)."

		dispatcher.utter_message(response)
		return [SlotSet('pos',pos)]

##pos_ition

class ActionReligion(Action):
	def name(self):
		return 'Action_Religion'

	def run(self, dispatcher, tracker, domain):
		rel = tracker.get_slot('rel')
		if rel == "religion":
			response = "To add, edit or delete religions in your system, go to Employee Portal > Religion or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/ReligionMaster/WebContent/index.html."
		elif rel == "my_profile":
			response = "To view your basic details, go to My Profile > Employee Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeMaster/WebContent/index.html#/Details/EmployeeList(50)."

		dispatcher.utter_message(response)
		return [SlotSet('rel',rel)]

##rel_gion


class ActionBand(Action):
	def name(self):
		return 'Action_Band'

	def run(self, dispatcher, tracker, domain):
		band = tracker.get_slot('band')
		if band == "band":
			response = "To add organization bands and define entitlements, go to Employee Portal > Band or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BandMaster/WebContent/index.html."
		elif band == "my_profile":
			response = "To view your basic details, go to My Profile > Employee Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeMaster/WebContent/index.html#/Details/EmployeeList(50)."

		dispatcher.utter_message(response)
		return [SlotSet('band',band)]

##ban_d

class ActionBlood(Action):
	def name(self):
		return 'Action_Blood'

	def run(self, dispatcher, tracker, domain):
		blood = tracker.get_slot('blood')
		if blood == "blood":
			response = "To add, edit, delete blood types as per your operation, go to Employee Portal > Blood Group or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BloodGroupMaster/WebContent/index.html."
		elif blood == "my_profile":
			response = "To view your basic details, go to My Profile > Employee Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeMaster/WebContent/index.html#/Details/EmployeeList(50)."

		dispatcher.utter_message(response)
		return [SlotSet('blood',blood)]

##blo_od

class ActionQualification(Action):
	def name(self):
		return 'Action_Qualification'

	def run(self, dispatcher, tracker, domain):
		qualifications = tracker.get_slot('qualifications')
		if qualifications == "qual":
			response = "To add, edit, delete qualification details, go to Employee Portal > Qualification or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/QualificationMaster/WebContent/index.html."
		elif qualifications == "qualificat_ion":
			response = "To add, edit, delete Educational details, go to Employee Portal > Educational Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EducationalDetails/WebContent/index.html."
		elif qualifications == "my_profile":
			response = "To view your basic details, go to My Profile > Employee Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeMaster/WebContent/index.html#/Details/EmployeeList(50)."

		dispatcher.utter_message(response)
		return [SlotSet('qualifications',qualifications)]

##qua_lifications

class ActionDesignation(Action):
	def name(self):
		return 'Action_Designation'

	def run(self, dispatcher, tracker, domain):
		designation = tracker.get_slot('designation')
		if designation == "designation":
			response = "To add, edit, delete organization designations details, go to Employee Portal > Designation or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/DesignationMaster/WebContent/index.html."
		elif designation == "my_profile":
			response = "To view your basic details, go to My Profile > Employee Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeMaster/WebContent/index.html#/Details/EmployeeList(50)."

		dispatcher.utter_message(response)
		return [SlotSet('designation',designation)]

##des_ignation

class ActionCountry(Action):
	def name(self):
		return 'Action_Country'

	def run(self, dispatcher, tracker, domain):
		country = tracker.get_slot('country')
		if country == "country":
			response = "To add edit or delete business operation countries, go to Employee Portal > Country or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/CountryMaster/WebContent/index.html."
		elif country == "region":
			response = "To add edit or delete regions, go to Employee Portal > Region or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RegionMaster/WebContent/index.html."
		elif country == "location":
			response = "To add edit or delete business operation locations, go to Employee Portal > Location or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/LocationMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('country',country)]

##cou_ntry

class ActionCostCenter(Action):
	def name(self):
		return 'Action_Cost_Center'

	def run(self, dispatcher, tracker, domain):
		cos_tcenter = tracker.get_slot('cos_tcenter')
		if cos_tcenter == "cost_center":
			response = "To view, edit, activate or deactivate cost centers, go to Employee Portal > Cost Center or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/CostCenterMaster/WebContent/index.html."
		elif cos_tcenter == "cost_center_incharge":
			response = "To view, edit, activate or deactivate cost center incharge details, go to Employee Portal > Cost Center Incharge or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/CostCenterIncharge/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('cos_tcenter',cos_tcenter)]

##cos_tcenter

class ActionLegalEntity(Action):
	def name(self):
		return 'Action_Legal_Entity'

	def run(self, dispatcher, tracker, domain):
		legalentity = tracker.get_slot('legalentity')
		if legalentity == "legal_entity":
			response = "To add, edit or delete your organization's legal entities, go to Employee Portal > Legal Entity or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/LegalEntityMaster/WebContent/index.html."
		elif legalentity == "terms_and_conditions":
			response = "To add, edit or delete your organization's terms and conditions, go to Employee Portal > Terms and Conditions or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TermsAndConditions/WebContent/index.html."
		elif legalentity == "organization_workflow":
			response = "To view organization workflow, go to Help > Organization Workflows or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/WorlflowApps/WebContent/index.html."
		elif legalentity == "system_workflow":
			response = "To view system workflow, go to Help > System Workflow or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/WorkFlowsFixed/WebContent/index.html."
		dispatcher.utter_message(response)
		return [SlotSet('legalentity',legalentity)]
##leg_al


class ActionIssueLetter(Action):
	def name(self):
		return 'Action_Issue_Letter'

	def run(self, dispatcher, tracker, domain):
		issueletter = tracker.get_slot('issueletter')
		if issueletter == "issue_letter":
			response = "To issue letter to employees, go to Employee Portal > Issue Letter or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeNotification/WebContent/index.html."
		elif issueletter == "letter_type":
			response = "To view letter type details, go to Employee Portal > Letter Type or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/LetterTypeMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('issueletter',issueletter)]

##iss_ueletter
##############################################################################################

#############################################################time management#############################################

class ActionTimesheet(Action):
	def name(self):
		return 'Action_Timesheet'

	def run(self, dispatcher, tracker, domain):
		timesheet = tracker.get_slot('timesheet')
		if timesheet == "time_sheet":
			response = "To enter your daily tasks, go to Time Management > Timesheet or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/TimesheetApp/WebContent/index.html."
		elif timesheet == "timesheet_report":
			response = "To view details of timesheet filled by employee, go to Time Management > Timesheet Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/TimesheetReport/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('timesheet',timesheet)]

##tim_esheet

class ActionLeave(Action):
	def name(self):
		return 'Action_Leave'

	def run(self, dispatcher, tracker, domain):
		leave = tracker.get_slot('leave')
		if leave == "short_leave_quota":
			response = "To view short leave quota, go to Time Management > Short Leave Quota or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShortLeaveQuota/WebContent/index.html."
		elif leave == "short_leaves_transaction":
			response = "To view short leave transaction, go to Time Management > Short Leave Transaction or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShortLeavesTransaction/WebContent/index.html."
		elif leave == "team_leave_report":
			response = "To view leave records of your team, go to Time Management > Team Leave Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveRequestHR/WebContent/index.html."
		elif leave == "leave_timeoff":
			response = "To apply or view leaves, go to Time Management > Leave/ Time-off or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveTransaction/WebContent/index.html."
		elif leave == "leave_approval_workflow":
			response = "To configure leave approval process, go to Time Management > Leave Approval Workflow or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveApprovalRule/WebContent/index.html."
		elif leave == "leave_balance_report":
			response = "To view leave balance report, go to Time Management > Leave Management Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveReport/WebContent/index.html."
		elif leave == "leave_group_master":
			response = "To assign an employee to a leave group, go to Time Management > Leave Group Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveEmployeeGroup/WebContent/index.html."
		elif leave == "leave_master":
			response = "To define leave types and rules, go to Time Management > Leave Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveMaster/WebContent/index.html."
		elif leave == "leave_request_approval":
			response = "To respond to your team's leave request, go to Time Management > Leave Request Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveTransactionApproval/WebContent/index.html."
		elif leave == "consolidated_leave_report":
			response = "To view leave record and status for entire organization, go to Employee Portal > Consolidated Leave Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ConsolidatedLeaveReport/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('leave',leave)]

##lea_ve

class ActionShift(Action):
	def name(self):
		return 'Action_Shift'

	def run(self, dispatcher, tracker, domain):
		shift = tracker.get_slot('shift')
		if shift == "shift_allocation":
			response = "To allocate shifts to user groups, go to Time Management > Shift Allocation or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftAllocation/WebContent/index.html."
		elif shift == "shift_details":
			response = "To define shift details, go to Time Management > Shift Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftDetails/WebContent/index.html."
		elif shift == "shift_master":
			response = "To create, edit or delete shift patterns, go to Time Management > Shift Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftMaster/WebContent/index.html."
		elif shift == "shift_pattern_master":
			response = "To define shift patterns, go to Time Management > Shift Pattern Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftPatternMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('shift',shift)]
####shi_ft
##
class ActionInouttime(Action):
	def name(self):
		return 'Action_Inouttime'

	def run(self, dispatcher, tracker, domain):
		inouttime = tracker.get_slot('inouttime')
		if inouttime == "approve_inout":
			response = "To approve manual in-out time, go to Time Management > Approve Manual In-out Time or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ApproveInOutManualTime/WebContent/index.html."
		elif inouttime == "manual_inout":
			response = "To update in-out time manually, go to Time Management > Manual In-out Time or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/InOutManualTime/WebContent/index.html."
		elif inouttime == "inout_time":
			response = "To view attendance records for self and team, go to Time Management > In-out Time or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeInOutRegisterEmp/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('inouttime',inouttime)]

##ino_uttime

class ActionAttendance(Action):
	def name(self):
		return 'Action_Attendance'

	def run(self, dispatcher, tracker, domain):
		attendance = tracker.get_slot('attendance')
		if attendance == "attendance_report":
			response = "To view columar attendance record for entire organization, go to Time Management > Attendance Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeInOutDataAdmin/WebContent/index.html."
		elif attendance == "attendance_report_register":
			response = "To view attendance records for entire organization, go to Time Management > Attendance Report Register or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeInOutRegister/WebContent/index.html."
		elif attendance == "inout_time":
			response = "To view attendance records for self and team, go to Time Management > In-out Time or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeInOutRegisterEmp/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('attendance',attendance)]

##att_endance

class ActionBusinessTravel(Action):
	def name(self):
		return 'Action_BusinessTravel'

	def run(self, dispatcher, tracker, domain):
		businesstravel = tracker.get_slot('businesstravel')
		if businesstravel == "business_travel_request":
			response = "To enter a business travel request, go to Time Management > Business Travel Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/LeaveTrnBusinessTrvl/WebContent/index.html."
		elif businesstravel == "business_travel_approval":
			response = "To approve a businees travel request, go to Time Managment > Business Travel Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/BusinessTravelApproval/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('businesstravel',businesstravel)]

##bus_inesstravel

class ActionCompoff(Action):
	def name(self):
		return 'Action_Compoff'

	def run(self, dispatcher, tracker, domain):
		compoff = tracker.get_slot('compoff')
		if compoff == "comp_credit_request":
			response = "To generate comp-off request, go to Time Management > Comp-off Credit Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmpCompOffRequest/WebContent/index.html."
		elif compoff == "comp_approval":
			response = "To approve a comp-off request, go to Time Management > Comp-off Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmpCompOffApproval/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('compoff',compoff)]

##com_poff

class ActionShift(Action):
	def name(self):
		return 'Action_Shift'

	def run(self, dispatcher, tracker, domain):
		shift = tracker.get_slot('shift')
		if shift == "shift_allocation":
			response = "To allocate shifts to user groups, go to Time Management > Shift Allocation or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftAllocation/WebContent/index.html."
		elif shift == "shift_details":
			response = "To define shift details, go to Time Management > Shift Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftDetails/WebContent/index.html."
		elif shift == "shift_master":
			response = "To create, edit or delete shift patterns, go to Time Management > Shift Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftMaster/WebContent/index.html."
		elif shift == "shift_pattern_master":
			response = "To define shift patterns, go to Time Management > Shift Pattern Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/ShiftPatternMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('shift',shift)]
##shi_ft

class ActionGroupmaster(Action):
	def name(self):
		return 'Action_Groupmaster'

	def run(self, dispatcher, tracker, domain):
		groupass = tracker.get_slot('groupass')
		if groupass == "emp_grp_ass":
			response = "To assign users to a group, go to Time Management > Employee Group Assignment or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeGroupAssignment/WebContent/index.html."
		elif groupass == "emp_grp_mas":
			response = "To create, edit or delete user groups, go to Time Management > Employee Group Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeGroupMaster/WebContent/index.html."
		elif groupass == "emp_grp_rules":
			response = "To define employee group rules, go to Time Management > Employee Group Rules or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmployeeGroupRules/WebContent/index.html ."
		elif groupass == "emp_subgrp_master":
			response = "To approve a comp-off request, go to Time Management > Comp-off Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/TM/EmpCompOffApproval/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('groupass',groupass)]

##gro_upass

#########################################################################################################################

#######################################################benefits, analytics and other stuff############################################

class ActionBenefit(Action):
	def name(self):
		return 'Action_Benefit'

	def run(self, dispatcher, tracker, domain):
		benefit = tracker.get_slot('benefit')
		if benefit == "benefit_master":
			response = "To add, edit, activate or deactivate employee benefits, go to Compensation and Benefits > Benefit Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BenefitMaster/WebContent/index.html."
		elif benefit == "benefit_parameter_master":
			response = "To set benefit parameters, go to Compensation and Benefits > Benefit Parameter Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BenefitParameterMaster/WebContent/index.html."
		elif benefit == "benefit_requests_approval":
			response = "To approve a benefit request, go to Compensation and Benefits > Benefit Requests Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BenefitTransactionApproval/WebContent/index.html."
		elif benefit == "employee_benefit_reprot":
			response = "To view employee benefit report, go to Compensation and Benefits > Employee Benefit Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeesBenefitReport/WebContent/index.html."
		elif benefit == "request_for_benefits":
			response = "To request for benefits, go to Compensation and Benefits > Request for Benefits or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BenefitTransactionWF/WebContent/index.html."
		elif benefit == "set_benefit_parameter":
			response = "To set benefit parameters, go to Compensation and Benefits > Set Benefit Parameter or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/AssignBenefitParameter/WebContent/index.html."
		elif benefit == "salary_structure":
			response = "To view your salary structure, go to Compensation and Benefits > Salary Structure or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/SalaryStructure_v1/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('benefit',benefit)]

##ben_efit

class ActionVeusage(Action):
	def name(self):
		return 'Action_Veusage'

	def run(self, dispatcher, tracker, domain):
		valeure = tracker.get_slot('valeure')
		if valeure == "ve_usage_dashboard":
			response = "To view vE usage dashboard, go to Data Analytics > vE Usage Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/vEUsageDashboard/WebContent/index.html."
		elif valeure == "ve_usage_report":
			response = "To view vE Usage Report, go to Data Analytics > vE Usage Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/VEUsageReport/WebContent/index.html."
		elif valeure == "ve_usage_trial_report":
			response = "To view trial user report, go to Data Analytics > vE Usage Trial Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/vEUsageTrailUserReport/WebContent/index.html."
		elif valeure == "trial_users_report":
			response = "To view trial user report, go to Data Analytics > Trial Users Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/TrialUsersReport/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('valeure',valeure)]

##val_eure

class ActionCount(Action):
	def name(self):
		return 'Action_Count'

	def run(self, dispatcher, tracker, domain):
		count = tracker.get_slot('count')
		if count == "employee_count":
			response = "To view the employees count, go to Data Analytics > Employee Count or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmpTotalCountReport/WebContent/index.html."
		elif count == "employee_list":
			response = "To view employee list, go to Data Analytics > Employee List or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeDetailsReport/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('count',count)]

##cou_nt

class ActionDashboard(Action):
	def name(self):
		return 'Action_Dashboard'

	def run(self, dispatcher, tracker, domain):
		dashboard = tracker.get_slot('dashboard')
		if dashboard == "active_users_dashboard":
			response = "To view active users count, go to Data Analytics > Active Users Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/ActiveEmpGraphReport/WebContent/index.html."
		elif dashboard == "revenue_profit_dashboard":
			response = "To view Revenue Profit Dashboard, go to Data Analytics > Revenue Profit Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RevenueProfitDashboard/index.html."
		elif dashboard == "ve_usage_dashboard":
			response = "To view vE usage dashboard, go to Data Analytics > vE Usage Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/vEUsageDashboard/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('dashboard',dashboard)]

##das_hboard

class ActionHelp(Action):
	def name(self):
		return 'Action_Help'

	def run(self, dispatcher, tracker, domain):
		help = tracker.get_slot('help')
		if help == "help_desk_incharge":
			response = "To assign help desk requests to your team members, go to ObiE > Help Desk Incharge or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/EmployeeHelpDesk/WebContent/index.html."
		elif help == "help_desk_report":
			response = "To run a report with the status of tickets logged by your team, go to ObiE > Help Desk Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/ConcernHelpDeskReport/WebContent/index.html."
		elif help == "help_desk_request":
			response = "To log in help desk request with respective departments, go to ObiE > Help Desk Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/ConcernsHelpdeskRequest/WebContent/index.html."
		elif help == "help_desk_review":
			response = "To review, assign and resolve all help desk tickets logged by your team, go to ObiE > Help Desk Review or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/ConcernsHelpdeskApproval/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('help',help)]

##hel_p

class ActionAppointment(Action):
	def name(self):
		return 'Action_Appointment'

	def run(self, dispatcher, tracker, domain):
		appointmentletter = tracker.get_slot('appointmentletter')
		if appointmentletter == "appointment_letter_template":
			response = "To create, duplicate, deactivate, view appointment letter template, go to Onboarding > Appointment Letter Template or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/OnBoarding/AppointmentTemplate/WebContent/index.html."
		elif appointmentletter == "generate_appointment_letter":
			response = "To choose a template and generate appointment letter, go to Onboarding > Generate Appointment Letter or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/OnBoarding/CandidateAppointmentApp/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('appointmentletter',appointmentletter)]
##app_ointmentletter

class ActionPerformance(Action):
	def name(self):
		return 'Action_Performance'

	def run(self, dispatcher, tracker, domain):
		performance = tracker.get_slot('performance')
		if performance == "annual_report":
			response = "To view annual report of all candidates, go to Performance Management > Annual Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/AnnualGoalReport/WebContent/index.html."
		elif performance == "performance_report":
			response = "To view performance report of all candiates, go to Performance Management > Performance Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/ReviewReport/WebContent/index.html."
		elif performance == "performance_review":
			response = "To review performance of your employees, go to Performance Management > Performance Review or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/PerformanceReview/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('performance',performance)]
##per_formance

class ActionGoals(Action):
	def name(self):
		return 'Action_Goals'

	def run(self, dispatcher, tracker, domain):
		goal = tracker.get_slot('goal')
		if goal == "assign_new_goals":
			response = "To assign new goals to you and your employees, go to Performance Management > Assign New Goals or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/MgrOrganizationGoals/WebContent/index.html."
		elif goal == "goal_plan_master":
			response = "To view goal plan master, go to Performance Management > Goal Plan Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/GoalPlanMaster/WebContent/index.html."
		elif goal == "goals_library":
			response = "To view goals library, go to Performance Management > Goals Library or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/GoalLibraryMaster/WebContent/index.html."
		elif goal == "track_your_goals":
			response = "To track your goals, go to Performance Management > Track Your Goals or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PMGM/EmpGoalsTrack/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('goal',goal)]

##goa_l

class ActionProbation(Action):
	def name(self):
		return 'Action_Probation'

	def run(self, dispatcher, tracker, domain):
		probation = tracker.get_slot('probation')
		if probation == "employee_probation_group_master":
			response = "To add, edit or delete probation groups, go to Probation > Employee Probation Group Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROB/EmpGrpAssign/WebContent/index.html."
		elif probation == "probation_approval":
			response = "To approve employees after probation period, go to Probation > Probation Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROB/EmpProbApproval/WebContent/index.html."
		elif probation == "probation_approval_workflow":
			response = "To configure probation approval workflow, go to Probation > Probation Approval Workflow Configuration or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROB/ConfigurationApp/WebContent/index.html."
		elif probation == "probation_level_master":
			response = "To configure probation level master, go to Probation > Probation Level Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROB/ProbationLevelMaster/WebContent/index.html."
		elif probation == "probation_period_master":
			response = "To access probation period master, go to Probation > Probation Period Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROB/ProbationPeriodMaster/WebContent/index.html."
		elif probation == "probation_report":
			response = "To view probation report, go to Probation > Probation Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROB/ProbationReport/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('probation',probation)]

##pro_bation

class ActionTask(Action):
	def name(self):
		return 'Action_Task'

	def run(self, dispatcher, tracker, domain):
		task = tracker.get_slot('task')
		if task == "task_backlog":
			response = "To view task backlogs, go to Project Management > Task Backlog or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROJ/TaskBacklog/WebContent/index.html."
		elif task == "task_backlog_report":
			response = "To view task backlog report, go to Project Management > Task Backlog Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROJ/TaskBacklogReport/WebContent/index.html."
		elif task == "task_list_details":
			response = "To view and update the status of pending tasks, go to Project Management > Task List Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/TaskListDetails/WebContent/index.html."
		elif task == "task_status_report":
			response = "To view your task status report, go to Project Management > Tasks Status Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/AssignTaskReport/WebContent/index.html."
		elif task == "my_todo_task":
			response = "To manage your task and works, go to Project Management > My To-do Task or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/HomeToDoList/WebContent/index.html."
		elif task == "assign_task":
			response = "To delegate or assign tasks, go to Project Management > Assign Task or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/HomeTaskListMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('task',task)]


##tas_k

class ActionPrjworkflow(Action):
	def name(self):
		return 'Action_Prjworkflow'

	def run(self, dispatcher, tracker, domain):
		prjworkflow = tracker.get_slot('prjworkflow')
		if prjworkflow == "project_workflow_request":
			response = "To view project workflow request, go to Project Management > Project Workflow Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROJ/ProjectWFRequest/WebContent/index.html."
		elif prjworkflow == "project_vertical":
			response = "To access project vertical master, go to Project Management > Project Vertical or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PROJ/ProjectVertical/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('prjworkflow',prjworkflow)]

##prj_workflow


class ActionPurchseorder(Action):
	def name(self):
		return 'Action_Purchseorder'

	def run(self, dispatcher, tracker, domain):
		purchaseorder = tracker.get_slot('purchaseorder')
		if purchaseorder == "purchase_approval_hr":
			response = "To approve HR purchase order, go to Purchase Order Management > Purchase Approval HR or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PR/PurchaseApprovalAdmin/WebContent/index.html."
		elif purchaseorder == "purchase_order_attachments":
			response = "To pin attachments to your purchase order, go to Purchase Order Management > Purchase Order Attachments or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PR/PurchaseRequestAttachments/WebContent/index.html."
		elif purchaseorder == "purchase_request":
			response = "To enter a purchase order request, go to Purchase Order Management > Purchase Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PR/PurchaseRequest/WebContent/index.html."
		elif purchaseorder == "purchase_request_approval":
			response = "To approve a purchase order request, go to Purchase Order Management > Purchase Request Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PR/PurchaseRequestApproval/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('purchaseorder',purchaseorder)]

##pur_chaseorder

class ActionRelationshipmgmt(Action):
	def name(self):
		return 'Action_Relationshipmgmt'

	def run(self, dispatcher, tracker, domain):
		relationshipmgmt = tracker.get_slot('relationshipmgmt')
		if relationshipmgmt == "relationship_dashboard":
			response = "To view your relations information filtered as per your requirements, go to Relationship Management > Realtionship Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RelationshipMeetingReport/WebContent/index.html."
		elif relationshipmgmt == "relationship_development":
			response = "To create and manage your business relationships, go to Relationship Management > Relationship Development or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RelationshipMeeting/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('relationshipmgmt',relationshipmgmt)]

##rel_ationshipmgmt


class ActionBusinessdev(Action):
	def name(self):
		return 'Action_Businessdev'

	def run(self, dispatcher, tracker, domain):
		businessdev = tracker.get_slot('businessdev')
		if businessdev == "business_development_report":
			response = "To view business development report, go to Relationship Management > Business Development Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RMDashboard/WebContent/index.html."
		elif businessdev == "business_vertical_master":
			response = "To add, edit, activate, deactivate business verticals, go to Relationship Management > Business Vertical Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/BusinessVerticalMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('businessdev',businessdev)]

##bus_inessdev


class ActionResignation(Action):
	def name(self):
		return 'Action_Resignation'

	def run(self, dispatcher, tracker, domain):
		resignation = tracker.get_slot('resignation')
		if resignation == "resignation_application":
			response = "To terminate an employee, go to Seperation > Resignation Application or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Separation/EmpResignRequest/WebContent/index.html."
		elif resignation == "resignation_request":
			response = "To submit resignation, go to Seperation > Resignation Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Separation/EmpResignRequest/WebContent/index.html."
		elif resignation == "seperation_configuration":
			response = "To configure seperation process, go to Seperation > Seperation Configuration or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Separation/ConfigurationApp/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('resignation',resignation)]
##res_ignation

##class ActionUserguide(Action):
##	def name(self):
##		return 'Action_Userguide'
##
##	def run(self, dispatcher, tracker, domain):
##		guide = tracker.get_slot('guide')
##		if guide == "user_guide_settings":
##			response = "To view user guide, go to Employee portal > User Guide Settings."
##		elif guide == "user_manual":
##			response = "To view user manual, go to Employee Portal > User Manual."
##
##		dispatcher.utter_message(response)
##		return [SlotSet('guide',guide)]

## - utter_userguide
## - actions.ActionUserguide
####gui_de
##  guide:
##    type: text		 - gui_de


class ActionRmmaster(Action):
	def name(self):
		return 'Action_Rmmaster'

	def run(self, dispatcher, tracker, domain):
		rmmaster = tracker.get_slot('rmmaster')
		if rmmaster == "rm_region_master":
			response = "To view a previous region or to create a new one, go to Relationship Management > RM Region Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/BKMAN/RegionMaster/WebContent/index.html."
		elif rmmaster == "rm_region_state_master":
			response = "To provide a state for your region, go to Relationship Management > RM Region State Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/BKMAN/RegionStateMapping/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('rmmaster',rmmaster)]
##rmm_aster

class ActionRevenue(Action):
	def name(self):
		return 'Action_Revenue'

	def run(self, dispatcher, tracker, domain):
		revenuefull = tracker.get_slot('revenuefull')
		if revenuefull == "revenue_master":
			response = "To view revenue details, go to Employee Portal > Revenue Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RevenueMaster/index.html."
		elif revenuefull == "revenue_report":
			response = "To view revenue report, go to Relationship Management > Revenue Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/EP/RevenueReport/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('revenuefull',revenuefull)]
##revenue

class ActionPayroll(Action):
	def name(self):
		return 'Action_Payroll'

	def run(self, dispatcher, tracker, domain):
		payroll = tracker.get_slot('payroll')
		if payroll == "wage_component_master":
			response = "To set wage components, go to Payroll > Wage Component Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/WageComponentMaster/WebContent/index.html."
		elif payroll == "tax_rate_master":
			response = "To configure tax deductions for a particular location, go to Payroll > Tax Rate Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/TaxRateMaster/WebContent/index.html."
		elif payroll == "discrepancy_report":
			response = "To view discrepancy report, go to Payroll > Discrepancy Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/AttendanceDiscrepanciesV1/WebContent/index.html."
		elif payroll == "pay_frequency_master":
			response = "To configure pay frequencies, go to Payroll > Pay Frequency Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/PayFrequencyMaster/WebContent/index.html."
		elif payroll == "payout_dashboard":
			response = "To view payout analytics, go to Payroll > Payout Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/AnalyticCharts/WebContent/index.html."
		elif payroll == "payroll_component":
			response = "To assign variable components to employees, go to Payroll > Payroll Component or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/PayrollComponent/WebContent/index.html."
		elif payroll == "payroll_employee_group":
			response = "To add emplooyees to payroll groups, go to Payroll > Payroll Employee Group or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmployeeGroupMaster/WebContent/index.html."
		elif payroll == "run_payroll":
			response = "To run payroll, go to Payroll > Run Payroll or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/RunPayroll/WebContent/index.html."
		elif payroll == "run_working_days":
			response = "To run working days, go to Employee Portal > Run Working Days or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/RunWorkingDays/WebContent/index.html."
		elif payroll == "salary_breakup":
			response = "To view the salary breakup, go to Payroll > Salary Breakup or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/SalaryBreakup/WebContent/index.html."
		elif payroll == "upload_working_days":
			response = "To upload working days, go to Payroll > Upload Working Days or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/SpecialCasesDays/WebContent/index.html."
		elif payroll == "block_employee_payroll":
			response = "To block employee payroll, go to Payroll > Block Employee Payroll or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/BlockEmployeePayroll/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('payroll',payroll)]
##pay_roll


class ActionDeclaration(Action):
	def name(self):
		return 'Action_Declaration'

	def run(self, dispatcher, tracker, domain):
		declaration = tracker.get_slot('declaration')
		if declaration == "wage_component_master":
			response = "To set wage components, go to Payroll > Wage Component Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/WageComponentMaster/WebContent/index.html."
		elif declaration == "tax_rate_master":
			response = "To configure tax deductions for a particular location, go to Payroll > Tax Rate Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/TaxRateMaster/WebContent/index.html."
		elif declaration == "discrepancy_report":
			response = "To view discrepancy report, go to Payroll > Discrepancy Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/AttendanceDiscrepanciesV1/WebContent/index.html."
		elif declaration == "pay_frequency_master":
			response = "To configure pay frequencies, go to Payroll > Pay Frequency Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/PayFrequencyMaster/WebContent/index.html."
		elif declaration == "payout_dashboard":
			response = "To view payout analytics, go to Payroll > Payout Dashboard or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/AnalyticCharts/WebContent/index.html."
		elif declaration == "payroll_component":
			response = "To assign variable components to employees, go to Payroll > Payroll Component or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/PayrollComponent/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('declaration',declaration)]
##dec_laration

class ActionCtc(Action):
	def name(self):
		return 'Action_Ctc'

	def run(self, dispatcher, tracker, domain):
		ctc = tracker.get_slot('ctc')
		if ctc == "employee_ctc":
			response = "To view employee CTC, go to Payroll > Employee CTC or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmployeeCTC/WebContent/index.html."
		elif ctc == "employee_deduction":
			response = "To view employee deduction, go to payroll > Employee Deduction or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmpDeduction/WebContent/index.html."
		elif ctc == "employee_payslip":
			response = "To view employee payslips, go to Payroll > Employee Payslip or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmployeePaySlip/WebContent/index.html."
		elif ctc == "employee_pf_account_details":
			response = "To view provident fund details, go to Payroll > Employee PF Account Details or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmpAccountDetail/WebContent/index.html."
		elif ctc == "employee_previous_income":
			response = "To view employee previous income, go to Payroll > Employee Previous Income or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmployeePreviousIncome/WebContent/index.html."
		elif ctc == "incentive_payment":
			response = "To view incentive payment, go to Payroll > Incentive Payment or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/EmpRefund/WebContent/index.html."
		elif ctc == "form16":
			response = "To fill or view your form 16, go to Payroll > Form 16 or https://i8bcc9c4c129.ap1.hana.ondemand.com/Reports/VHR_PAYROLL/WebContent/index.html."
		elif ctc == "arrear_payment":
			response = "To view arrear payment, go to Payroll > Arrear Payment or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/ArrearPayment/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('ctc',ctc)]
##ct_c

class ActionAustralia(Action):
	def name(self):
		return 'Action_Australia'

	def run(self, dispatcher, tracker, domain):
		australia = tracker.get_slot('australia')
		if australia == "australia_payslip":
			response = "To view australia payslip, go to Payroll > Australia Payslip or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/AustraliaSalaryEMP/WebContent/index.html."
		elif australia == "australia_payslip_configuration":
			response = "To configure australia payslip, go to Payroll > Australia Payslip Configuration or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/PRL/AustraliaSalary/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('australia',australia)]
##aus_tralia


class ActionExternal(Action):
	def name(self):
		return 'Action_External'

	def run(self, dispatcher, tracker, domain):
		external = tracker.get_slot('external')
		if external == "external_client_status":
			response = "To update the status of candidates, go to Talent Management > External Client Status or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/ExternalClientStatus/WebContent/index.html."
		elif external == "parser_configuration":
			response = "To activate or deactivate parsers, go to Talent Management > Parser Configuration or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/ParserConfiguration/WebContent/index.html."
		elif external == "posted_job":
			response = "To configure australia payslip, go to Talent Management > Posted Job or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/JobPosting/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('external',external)]
##ext_ernal


class ActionInterview(Action):
	def name(self):
		return 'Action_Interview'

	def run(self, dispatcher, tracker, domain):
		interview = tracker.get_slot('interview')
		if interview == "loi_template":
			response = "To generate loi template, go to Talent Management > LOI Template or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/LOITemplate/WebContent/index.html."
		elif interview == "offer_approval":
			response = "To approve job offer, go to Talent Management > Offer Approval or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/OfferApproval/WebContent/index.html."
		elif interview == "joinings_report":
			response = "To see joinings report, go to Talent Management > Joinings Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/TotalJoiningsReport/WebContent/index.html."
		elif interview == "candidate_report":
			response = "To see candidate report, go to Talent Management > Candidate Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/RequisitionReport/WebContent/index.html."
		elif interview == "add_modify_candidates":
			response = "To add/ modify candidates, go to Talent Management > Add/Modify Candidates or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/CandidateCV/WebContent/index.html."
		elif interview == "schedule_interviews":
			response = "To schedule interviews, go to Talent Management > Schedule Interviews or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/TagCandidate/WebContent/index.html."
		elif interview == "interview_rating":
			response = "To view, create interview ratings, go to Talent Management > Interview Rating or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/CandidateRating/WebContent/index.html."


		dispatcher.utter_message(response)
		return [SlotSet('interview',interview)]
##int_erview

class ActionRecruitment(Action):
	def name(self):
		return 'Action_Recruitment'

	def run(self, dispatcher, tracker, domain):
		recruitement = tracker.get_slot('recruitement')
		if recruitement == "recruitment_dashboard":
			response = "To view recruitement dashboard, go to Talent Management > Recruitement Dashbaord or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/DashboardV2/WebContent/index.html."
		elif recruitement == "requisition_approval":
			response = "To approve a requisition request, go to Talent Management > Requisition Request or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/RequisitionApprovalConfiguration/WebContent/index.html."
		elif recruitement == "requisition_payout":
			response = "To create requisition payout, go to Talent Management > Requisition Payout or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/RequisitionPayout/WebContent/index.html."
		elif recruitement == "job_requisition":
			response = "To create a job requisition request, go to Talen Management > Job Requisition or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/EmployeeRecruitment/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('recruitement',recruitement)]
##rec_ruitement


class ActionResume(Action):
	def name(self):
		return 'Action_Resume'

	def run(self, dispatcher, tracker, domain):
		resume = tracker.get_slot('resume')
		if resume == "resume_bulk_upload":
			response = "To access candidate resume bulk upload, go to Talent Management > Resume Bulk Upload or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/CandidateBulkCV/WebContent/index.html."
		elif resume == "resume_repository_configuration":
			response = "To configure resume repository, go to Talent Management > Resuem Repository Configuration or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/RCM/ResumeStorageConfig/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('resume',resume)]
##res_ume


class ActionAgeing(Action):
	def name(self):
		return 'Action_Ageing'

	def run(self, dispatcher, tracker, domain):
		ageing = tracker.get_slot('ageing')
		if ageing == "average_ageing_report":
			response = "To view average ageing report, go to Talent Management > Average Ageing Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/AverageAgeingReport/WebContent/index.html."
		elif ageing == "candidate_ageing_report":
			response = "To view candidate ageing report, go to Talent Management > Candidate Ageing Report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/AgeingReport/WebContent/index.html."
		elif ageing == "consolidated_job_report":
			response = "To view consolidated job report, go to Talent Management > consolidated job report or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/RequisitionSummary/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('ageing',ageing)]
##age_ing

class ActionRcm(Action):
	def name(self):
		return 'Action_Rcm'

	def run(self, dispatcher, tracker, domain):
		rcm = tracker.get_slot('rcm')
		if rcm == "rcm_client_master":
			response = "To create a RCM client, go to Talent Management > RCM Client Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/RCMClientMaster/WebContent/index.html."
		elif rcm == "tenure_master":
			response = "To view tenure details, go to Talent Management > Tenure Master or https://i8bcc9c4c129.ap1.hana.ondemand.com/ValeurHR/VHRHRM/Recruitment/TenureMaster/WebContent/index.html."

		dispatcher.utter_message(response)
		return [SlotSet('rcm',rcm)]
##rc_m


class ActionMessagesDatabases(Action):
	def name(self):
		return 'Action_Messages_Databases'

	def run(self, dispatcher, tracker, domain):
		json_data = open("message_store.json").read()
		data = json.loads(json_data)
		k = list(data.keys())[-1]
		v = list(data.values())[-1]
		kv = {k:v}
		big_data = [[k],kv]
		new_data = json.dumps(big_data)
		api_endpoint = "https://f84cc1353869.ap1.hana.ondemand.com/ValeurHR/VHRHRM/ChatBot/WebContent/backendArtifacts/xsjs/InsertBotData.xsjs"
		requests.post(url = api_endpoint,data = new_data, auth=HTTPBasicAuth("Val_dev1", "superAdminDev@1234"))

#################################################################################################################################
class ActionWeather(Action):
	def name(self):
		return 'Action_Weather'

	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = '5434c543a23c48ec80c91243180908'
		client = ApixuClient(api_key)

		weather_location = tracker.get_slot('weather_location')
		current = client.getCurrentWeather(q=weather_location)

		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)

		dispatcher.utter_message(response)
		return [SlotSet('weather_location',weather_location)]

class ActionSlotReset(Action):
    def name(self):
        return 'Action_Slot_Reset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
