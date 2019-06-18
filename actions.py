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
        time.sleep(1)
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


class ActionRestaurant(FormAction):

    RANDOMIZE = True

    REQUIRED_FIELDS = [
        EntityFormField("people", "people"),
        EntityFormField("location", "location"),
        EntityFormField("price", "price"),
        EntityFormField("cuisine", "cuisine")
    ]

    OPTIONAL_FIELDS = [
        EntityFormField("outdoor_seating", "outdoor_seating"),
        EntityFormField("reservations", "reservations"),
        EntityFormField("date_suitable", "date_suitable")
    ]

    def name(self):
        return "action_restaurant"

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_finish')
        return []


class ActionHotel(FormAction):

    REQUIRED_FIELDS = [
        EntityFormField("people", "people"),
        EntityFormField("location", "location"),
        EntityFormField("price", "price"),
        EntityFormField("date", "start_date"),
        EntityFormField("date", "end_date")
    ]

    OPTIONAL_FIELDS = [
        EntityFormField("has_gym", "has_gym"),
        EntityFormField("has_spa", "has_spa"),
        EntityFormField("breakfast", "breakfast")
    ]

    def name(self):
        return "action_hotel"

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_finish')
        return []


class ActionSearchRestaurant(Action):

    def name(self):
        return "action_search_restaurant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_search')
        restaurant_api = RestaurantAPI()
        restaurant = restaurant_api.search(tracker.get_slot('cuisine'))

        return [SlotSet('restaurant', restaurant)]


class ActionSearchHotel(Action):

    def name(self):
        return "action_search_hotel"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_search')
        hotel_api = HotelAPI()
        hotel = hotel_api.search(tracker.get_slot('location'))

        return [SlotSet('hotel', hotel)]


class ActionExplain(Action):

    def name(self):
        return "action_explain"

    def run(self, dispatcher, tracker, domain):
        # TODO: actually implement this
        dispatcher.utter_message('This means blabla')

        return []