# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import os
import openai
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


class ActionCreateImage(Action):

    def name(self) -> Text:
        return "action_create_image"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prompt = tracker.latest_message['text']

        openai.api_key = OPENAI_API_KEY
        response = openai.Image.create(prompt=prompt,
                                       n=1,
                                       size="512x512")

        url_img = response.get("data")[0].get("url")

        img = requests.get(url_img).content

        with open("img_create/img_response.jpg", 'wb') as handler:
            handler.write(img)

        return []
