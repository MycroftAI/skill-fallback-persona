# Copyright 2017 Mycroft AI, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft import FallbackSkill, intent_handler
import requests
import urllib


class FallbackPersonaSkill(FallbackSkill):
    def __init__(self):
        FallbackSkill.__init__(self)
        self.persona_url = "http://training.mycroft.ai/persona/api/persona/?"

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
