from typing import Any, Dict, List, Optional, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecuted, FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher

from src.mtx_request.actions.action_field import ActionField


class RequestFieldSelectLocation(ActionField):

    def __init__(self, fieldName):
        self.fieldName = fieldName

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        events: List[Dict[Text, Any]]
    ) -> List[Dict[Text, Any]]:
        services = self._serviceRepository()

        activeSlot = self._getActiveSlot(tracker)
        if not self._isSlotActive(activeSlot):
            self.activate(events)

            dispatcher.utter_message(
                'Introduce una localización. Ejemplo: Calle Aguacate, 41, Madrid'
            )
        else:
            message = tracker.latest_message.get('text').lower()

            print(message)

            events.append(SlotSet('request_location', message))
            self.deactivate(events)

        return events

    def _serviceRepository(self) -> List[Text]:
        return [
            'Zonas Verdes',
            'Fuentes ornamentales',
            'Fuentes de beber',
            'Recogida de muebles',
        ]
