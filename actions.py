from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class BestPhone(Action):
    def name(self):
        return 'best_phone'

    def run(self, dispatcher, tracker, domain):

        phn=tracker.get_slot('phone')
        reponse="This is the best phone"
        dispatcher.utter_message(reponse)
        dispatcher.utter_message("This is my response")
        return [SlotSet('phone',phn)]
