from typing import Any, Dict, List, Optional, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecuted, FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher

from src.mtx_request.actions.action_field import ActionField


class RequestFieldSelectService(ActionField):

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
                'Para continuar, necesito clasificar tu aviso en una de las siguientes categorías:'
            )

            for service in services:
                dispatcher.utter_message(service)

            dispatcher.utter_message(
                'Escribe algunas palabras de la categoría que mejor encaja, y te ayudaré a seleccionarla.'
            )
        else:
            message = tracker.latest_message.get('text').lower()

            print(message)

            validServices = list(
                filter(
                    lambda service: service.lower().find(
                        message) >= 0, services
                )
            )

            if len(validServices) == 1:
                events.append(SlotSet('request_service', validServices[0]))
                self.deactivate(events)

                dispatcher.utter_message(
                    'Elegida la categoría {}.'.format(validServices[0])
                )

            elif len(validServices) > 1:
                buttons = []

                for validService in validServices:
                    buttons.append({
                        'title': validService,
                        'payload': validService
                    })

                if len(buttons) > 0:
                    dispatcher.utter_message(
                        text='Selecciona la opción que se ajuste mejor:',
                        buttons=buttons
                    )

        return events

    def _serviceRepository(self) -> List[Text]:
        return [
            'Zonas Verdes',
            'Fuentes ornamentales',
            'Fuentes de beber',
            'Recogida de muebles',
        ]
