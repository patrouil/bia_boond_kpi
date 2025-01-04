from  functools import cache
from boond.boond_api import BoondApi
from boond.entity.action_entity import ActionEntity
from boond.entity.entity_actions import EntityActions


class LastResourceActionQuery:
    paramdict_hr = {
        'countTopTypes': 10,
        'maxResults': 30,
        'order': 'desc',
        'sort': 'startDate',
        'actionTypes' : '[9,80,83]'         # suivi Mission , Entretient RH, Point RH
    }
    paramdict_any = {
    'countTopTypes': 10,
    'maxResults': 10,
    'order': 'desc',
    'sort': 'creationDate'
}
    def __init__(self, api: BoondApi):
        self.api = api

    @cache
    def get_rh_actions(self, entity_id : str)->EntityActions:
        plan = self.api.getResourceActionsById(entity_id, self.paramdict_hr)
        return plan


    @cache
    def get_any_actions(self, entity_id : str)->[ActionEntity]:
        plan = self.api.getResourceActionListById(entity_id, self.paramdict_any)
        return list(plan)
