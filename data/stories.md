## greet
* greet
  - utter_introduce_bot
  - utter_offer_help
> check_user_question

## user asks for help
> check_user_question
* ask_for_help
  - utter_show_what_bot_can_do

<!-- ## user ask for request creation / HAPPY PATH
> check_user_question
* create_request
  - action_request_slots_reset
  - slot{"current_iterative_action": null}
  - utter_create_request
  - description_form
  - form{"name": "description_form"}
  - form{"name": null}
  - action_get_user_data
  - action_get_jurisdiction
  - iter_action_select_request_service
  - iter_action_select_location
  - iter_action_add_pictures
  - utter_request_summary
  - utter_offer_help
> check_user_question -->

## user ask for request creation
> check_user_question
* create_request
  - utter_create_request
  - iter_action_create_request
  - utter_offer_help
> check_user_question
