from typing import Any, Dict, List, Optional, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecuted, FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher

from src.mtx_request.actions.action_field import ActionField


class RequestFieldFetchJurisdiction(ActionField):

    def __init__(self, fieldName):
        self.fieldName = fieldName

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        events: List[Dict[Text, Any]]
    ) -> List[Dict[Text, Any]]:

        events.append(
            SlotSet(
                self.fieldName,
                self._jurisdictionRepository()
            )
        )

        # activeSlot = self._getActiveSlot(tracker)
        # if not self._isSlotActive(activeSlot):
        #     self.activate(events)

        #     events.append(
        #         SlotSet(
        #             self.fieldName,
        #             self._jurisdictionRepository()
        #         )
        #     )
        # else:
        #     self.deactivate(events)

        return events

    def _jurisdictionRepository(self) -> Text:
        return 'es.madrid'
