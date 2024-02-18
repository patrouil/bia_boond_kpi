from  functools import cache
from boond.boond_api import BoondApi
from boond.entity.entity_actions import EntityActions


class LastResourceActionQuery:
    paramdict = {
        'countTopTypes': 10,
        'maxResults': 30,
        'order': 'desc',
        'sort': 'startDate',
        'actionTypes' : '[9,80,83]'         # suivi Mission , Entretient RH, Point RH
    }

    def __init__(self, api: BoondApi):
        self.api = api

    @cache
    def get_rh_actions(self, entity_id : str)->EntityActions:
        plan = self.api.getResourceActionsById(entity_id, self.paramdict)
        return plan
