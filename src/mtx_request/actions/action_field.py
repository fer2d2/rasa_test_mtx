from rasa_sdk.events import SlotSet


class ActionField():
    fieldName = None

    def activate(self, events):
        """Enabling a slot will repeat the run method until the slot is disabled with `deactivate()`"""
        events.append(SlotSet('active_field', self.fieldName))

    def deactivate(self, events):
        """Disabling a slot will stop repeating the run method for an active slot"""
        events.append(SlotSet('active_field'))

    def _isSlotActive(self, currentSlot):
        return self.fieldName == currentSlot

    def _getActiveSlot(self, tracker):
        return tracker.get_slot('active_field')
