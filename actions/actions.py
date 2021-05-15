# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

#****************************************************
class ActionSaveOrigin(Action):
	def name(self):
		return "action_save_origin"

	def run(self, dispatcher, tracker, domain):
		orig = next(tracker.get_latest_entity_values("location"), None)
		print("Origin to Save ===============> ", orig)
		if not orig:
			dispatcher.utter_message("Please enter a valid airport code")
			return [UserUtteranceReverted()]
		return [SlotSet('origin',orig)]
#*****************************************************
class ActionSaveDestination(Action):
	def name(self):
		return "action_save_destination"

	def run(self, dispatcher, tracker, domain):
		# value = next((x["value"] for x in tracker.latest_message.entities if x['entity'] == 'location'), None)
		# return [SetSlot("destination", value)]
		dest = next(tracker.get_latest_entity_values("location"), None)
		if not dest:
			dispatcher.utter_message("Please enter a valid airport code")
			return [UserUtteranceReverted()]
		return [SlotSet('destination',dest)]

#*****************************************************
class ActionSaveDate(Action):
	def name(self):
		return "action_save_date"

	def run(self, dispatcher, tracker, domain):
		value = next((x["value"] for x in tracker.latest_message.entities if x['entity'] == 'date'), None)
		return [SetSlot("date", value)]		
#*****************************************************

# class SaveOrigin(Action):
# 	def name(self)-> Text:
# 		return 'action_save_origin'
		
# 	def run(self, dispatcher, tracker, domain):
# 		orig = next(tracker.get_latest_entity_values("location"), None)
# 		if not orig:
# 			dispatcher.utter_message("Please enter a valid airport code")
# 			return [UserUtteranceReverted()]
# 		return [SlotSet('from',orig)]

