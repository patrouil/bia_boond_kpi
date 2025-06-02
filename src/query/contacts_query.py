
from boond import BoondApi
from boond.entity.entity_contacts import EntityContacts


class ContactsQuery:
    # order attrib get an already sorted list.
    # https://ui.boondmanager.com/contacts?
    # columns=%5B%22lastName%22%2C%22function%22%2C%22company%22%2C%22state%22%2C%22lastAction%22%2C%22updateDate%22%5D&flags=%5B%228%22%5D&order=asc&returnMoreData=%5B%22lastAction%22%5D&saveSearch=true

    # endDate=2024-05-31&narrowPerimeter=false&occupationGradient=false&order=asc&perimeterPoles=%5B%224%22%5D&perimeterType=projects&period=monthly&positioningPeriod=created&regroup=false&reportingAvailability=asc&saveSearch=true&showContracts=false&sort=availability&startDate=2024-01-01

    paramdict = {
        "columns": '[lastName, function, company, state, lastaction, updateDate]',
        "flags": '[8]',
        'returnMoreData': '[lastAction]',  # en mission / futur inter co
        'maxResults': '300'
    }

    def __init__(self, api: BoondApi, flag_id: str=None):
        self.api = api

        if flag_id is not None : self.paramdict['flags'] = '['+flag_id+']'
        # otherwire  there is no perimeterPoles parameter
        return

    def getContacts(self ) -> EntityContacts:
        # start date is start of month

        plan = self.api.getContacts(self.paramdict)
        return plan
