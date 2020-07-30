from typing import Any, Dict, List, Optional, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecuted, FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher

from src.mtx_request.actions.request_field_fetch_jurisdiction import RequestFieldFetchJurisdiction
from src.mtx_request.actions.request_field_select_service import RequestFieldSelectService
from src.mtx_request.actions.request_field_select_location import RequestFieldSelectLocation


class IterActionCreateRequest(Action):
    ACTION_NAME = 'iter_action_create_request'

    FIELDS = [
        # 'user_data',
        'request_jurisdiction',
        # 'request_jurisdiction_id',
        # 'request_services',
        'request_service',
        'request_location',
        # 'request_description',
        # 'request_additional_data',
        # 'request_pictures',
        # 'request_url',
    ]

    MAPPINGS = {
        # 'user_data': 1,
        'request_jurisdiction': RequestFieldFetchJurisdiction('request_jurisdiction'),
        # 'request_jurisdiction_id': 3,
        # 'request_services': 4,
        'request_service': RequestFieldSelectService('request_service'),
        'request_location': RequestFieldSelectLocation('request_location'),
        # 'request_description': 7,
        # 'request_additional_data': 8,
        # 'request_pictures': 9,
        # 'request_url': 10,
    }

    def name(self) -> Text:
        return self.ACTION_NAME

    def _isFieldFilled(self, field: Text, tracker: Tracker):
        return tracker.get_slot(field) is not None

    def nextField(self, tracker: Tracker):
        for field in self.FIELDS:
            if not self._isFieldFilled(field, tracker):
                return field
        return None

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        events = []

        self._activateAction(events, tracker)

        field = self.nextField(tracker)

        if field is None:
            self._deactivateAction(events)
            self._deactivateAllSlots(events)

            # TODO jump to next action
        # elif tracker.latest_message['intent'].get('name') == 'stop':
        #     events.append(SlotSet('current_iterative_action'))
        else:
            events = self.MAPPINGS.get(field).run(
                dispatcher,
                tracker,
                domain,
                events
            )

        return events

    def _getActiveSlot(self, tracker):
        return tracker.get_slot('active_field')

    def _getActiveAction(self, tracker):
        return tracker.get_slot('active_action')

    def _activateAction(self, events, tracker):
        if self._getActiveAction(tracker) != 'active_action':
            events.append(SlotSet('active_action', self.ACTION_NAME))

    def _deactivateAction(self, events):
        events.append(SlotSet('active_action'))

    def _deactivateAllSlots(self, events):
        for field in self.FIELDS:
            events.append(SlotSet(field))
