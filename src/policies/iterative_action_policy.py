import logging
from typing import Any, Dict, List, Optional, Text, Union

from rasa.core.actions.action import ACTION_LISTEN_NAME
from rasa.core.domain import Domain
from rasa.core.featurizers import TrackerFeaturizer
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.trackers import DialogueStateTracker
from rasa_sdk import Tracker

logger = logging.getLogger(__name__)

DEFAULT_PRIORITY = 15


class IterativeActionPolicy(MemoizationPolicy):
    """Policy which handles prediction of Iterative Actions (Multiple response controls, complex fields selection, …)."""

    def __init__(
        self,
        featurizer: Optional[TrackerFeaturizer] = None,
        priority: int = DEFAULT_PRIORITY,
        lookup: Optional[Dict] = None,
    ) -> None:
        super().__init__(
            featurizer=featurizer, priority=priority, max_history=2, lookup=lookup
        )

    def predict_action_probabilities(self, tracker: Tracker, domain):
        """Predicts the corresponding iterative action if there is an active one. It checks the `active_action` slot."""

        result = self._default_predictions(domain)
        activeAction = tracker.get_slot('active_action')

        if activeAction:
            logger.debug(
                "There is an iterative action active: {}".format(
                    activeAction
                )
            )

            if tracker.latest_action_name == ACTION_LISTEN_NAME:
                idx = domain.index_for_action(activeAction)
                result[idx] = 1.0

            elif tracker.latest_action_name == activeAction and tracker.get_slot('active_field') is not None:
                idx = domain.index_for_action(ACTION_LISTEN_NAME)
                result[idx] = 1.0

            elif tracker.latest_action_name == activeAction and tracker.get_slot('active_field') is None:
                idx = domain.index_for_action(activeAction)
                result[idx] = 1.0
        else:
            logger.debug("There is no active iterative action")

        return result

    def persist(self, path: Text) -> None:
        pass

    @classmethod
    def load(cls, path: Text) -> "MemoizationPolicy":
        return cls()
