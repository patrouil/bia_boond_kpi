import datetime

from boond.boond_api import BoondApi
from boond.entity.reporting_production_plans import ReportingProductionPlans


class ProductionPlanQuery:
    # order attrib get an already sorted list.
    # endDate=2024-05-31&narrowPerimeter=false&occupationGradient=false&order=asc&perimeterPoles=%5B%224%22%5D&perimeterType=projects&period=monthly&positioningPeriod=created&regroup=false&reportingAvailability=asc&saveSearch=true&showContracts=false&sort=availability&startDate=2024-01-01

    paramdict = {
        "narrowPerimeter": "false",
        'resourceTypes': '[1,0]',  # consultant interne / externe
        'resourceStates': '[1,2]',  # en mission / futur inter co
        'perimeterType': 'projects',
        'perimeterPoles': '[1]',  # pole Patrick (@TODO rendre parametrable)
        'period': 'monthly',
        'order': 'asc',
        'sort': 'availability',
        'endDate': '2024-12-31',
        'startDate': '2024-01-01',
        'reportingAvailability': 'asc',
        'maxResults': '300'
    }

    def __init__(self, api: BoondApi, poles: str):
        self.api = api
        if poles is not None : self.paramdict['perimeterPoles'] = poles
        return

    def getProdPlan(self) -> ReportingProductionPlans:
        # start date is start of month
        t = datetime.date.today()
        t = t + datetime.timedelta(days=-31)  # remove a month
        t = t.replace(day=1)  # then start of this month
        beg = t.isoformat()
        self.paramdict['startDate'] = beg
        # end Date is plus one year.
        t = t.replace(year=t.year + 1)
        end = t.isoformat()
        self.paramdict['endDate'] = end
        plan = self.api.getReportingProductionPlan(self.paramdict)
        return plan
