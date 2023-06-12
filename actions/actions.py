# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# chainBotHackathon*123


# This is a simple example for a custom action which utters "Hello World!"
import os
import json
import openai
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# STUARY_API_KEY = os.environ["STUARY_API_KEY"]
FILE_IMG = os.environ["FILE_IMG"]


class ActionCreateImage(Action):

    def name(self) -> Text:
        return "action_create_image"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prompt = tracker.latest_message['text']

        # openai.api_key = OPENAI_API_KEY
        # response = openai.Image.create(prompt=prompt[14:],
        #                                n=1,
        #                                size="512x512")
        #
        # url_img = response.get("data")[0].get("url")
        #
        # img = requests.get(url_img).content
        #
        # with open("img_create/img_response.jpg", 'wb') as handler:
        #     handler.write(img)
        #
        # url = "https://upload.estuary.tech/content/add"
        #
        # payload = {}
        # headers = {'Accept': 'application/json',
        #            'Authorization': f"Bearer {STUARY_API_KEY}"}
        # files = [('data',
        #           ('file',
        #            open(f'{FILE_IMG}/img_response.jpg', 'rb'),
        #            'application/octet-stream'))]
        #
        # response = requests.request("POST", url, headers=headers, data=payload, files=files)
        #
        # cid = eval(response.text).get("cid")

        # dispatcher.utter_message(text=f"{prompt[14:]} image in: /img_create/img_response.jpg")
        bot_response = {"original_message": f"{prompt}"}
        json_response = json.dumps(bot_response)
        dispatcher.utter_message(text=str(json_response))

        return []


class ActionWalletBalance(Action):

    def name(self) -> Text:
        return "action_wallet_balance"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        token = tracker.latest_message['text']

        dispatcher.utter_message(text=f"You balance in {token} is 0.1")

        return []
