
from  functools import cache

from boond.boond_api import BoondApi
from boond.entity.action_entity import ActionEntity

class ActionsQuery:
    client_actions_param = {
        'countTopTypes': 10,
        'maxResults': 30,
        'order': 'desc',
        'sort': 'startDate',
        'actionTypes': '[11]'  # suivi Mission
    }

    common_actions_param = {
        'maxResults': '30',
        'order': 'desc',
        'sort': 'startDate'
    }

    def __init__(self, api: BoondApi):
        self.api = api

    def get_client_actions(self, client_id: str) -> [ActionEntity]:
        plan = self.api.getContactActionsById(client_id, self.client_actions_param)
        return plan

    def get_candidate_actions(self, entity_id: str) -> [ActionEntity]:
        plan = self.api.getCandidateActionListById(entity_id, self.common_actions_param)
        return plan
