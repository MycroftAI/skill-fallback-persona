from adapt.intent import IntentBuilder
from mycroft import FallbackSkill, intent_handler
import requests
import urllib


class FallbackPersonaSkill(FallbackSkill):
    def __init__(self):
        FallbackSkill.__init__(self)
	self.persona_url = "http://precise.mycroft.ai/persona/api/persona/?"

    def initialize(self):
	self.register_fallback(self.handle_fallback_persona, 8)

    def handle_fallback_persona(self, message):
	query = message.data['utterance']
	query_obj = {"query": query}
        url_encode = urllib.urlencode(query_obj)
	response_obj = requests.get(self.persona_url + url_encode).json()
	if float(response_obj['confidence']) < 0.7:
	    return False
        response = response_obj['response']
        self.speak(response)
	return True


def create_skill():
    return FallbackPersonaSkill()

