
from  functools import cache

from boond.boond_api import BoondApi
from boond.entity.entity_actions import EntityActions


class LastClientActionQuery:
    paramdict = {
        'countTopTypes': 10,
        'maxResults': 30,
        'order': 'desc',
        'sort': 'startDate',
        'actionTypes': '[11]'  # suivi Mission
    }

    def __init__(self, api: BoondApi):
        self.api = api

    @cache
    def get_client_actions(self, client_id: str) -> EntityActions:
        plan = self.api.getContactActionsById(client_id, self.paramdict)
        return plan
