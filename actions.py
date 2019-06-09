# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time
import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(
            requests.get("https://api.chucknorris.io/jokes/random").text
        )  # make an api call
        joke = request["value"]  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

# this action will add classification questions to the question queue stack

class ActionClassifyInsurance(Action):
    def name(self):
        # define the name of the action
        return "classify_insurance"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        xaa = "Classify Insurance"
        time.sleep(3)
        dispatcher.utter_message(xaa)
        return print(xaa)

class ActionFetchInsurancePolicyQuestions(Action):
    def name(self):
        # define the name of the action
        return "fetch_insurance_policy_questions"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        xaa = []
        request = json.loads(
            requests.get("https://myrpcendpoint.internal/policyquery").text
        )  # make an api call
        policy = request["question"]  # extract a joke from returned json response
        dispatcher.utter_message(policy)  # send the message back to the user
        return []

class ActionStateChecker(Action):
    def name(self):
        # define the name of the action
        return "state_checker"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        xaa = []
        # this will support conditional logic to find the next question
        # based on state of the current policy information
