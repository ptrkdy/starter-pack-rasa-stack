## request_policy
* request_restaurant
    - activate_restaurant
    - slot{"active_plan": true}
    - slot{"switch": false}
    - slot{"cuisine": "mexican"}
    - deactivate_plan
    - slot{"active_plan": false}
    - slot{"plan_complete": false}
    - utter_happy
* chitchat
    - utter_chitchat
* request_hotel
    - activate_hotel

## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 

## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 
## story_buy_insurance
* buy_insurance
 - utter_buy_insurance
 - classify_insurance
 

## story_joke_01
* joke
 - action_joke
 
## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 