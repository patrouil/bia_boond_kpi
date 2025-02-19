import datetime

from boond.boond_api import BoondApi
from boond.entity.reporting_production_plans import ReportingProductionPlans
from boond.entity.resource_entity import ResourceEntity


class ProductionPlanQuery:
    # order attrib get an already sorted list.
    # endDate=2024-05-31&narrowPerimeter=false&occupationGradient=false&order=asc&perimeterPoles=%5B%224%22%5D&perimeterType=projects&period=monthly&positioningPeriod=created&regroup=false&reportingAvailability=asc&saveSearch=true&showContracts=false&sort=availability&startDate=2024-01-01
    # https://ui.boondmanager.com/api/reporting-production-plans?endDate=2024-04-30&maxResults=30&narrowPerimeter=false&occupationGradient=false&order=asc&page=1&perimeterPoles=4&perimeterType=resources&period=monthly&positioningPeriod=created&regroup=false&reportingAvailability=asc&saveSearch=true&showContracts=false&sort=availability&startDate=2023-11-01
    paramdict = {
        'resourceTypes': '[1,0]',  # consultant interne / externe
        'resourceStates': '[1,2]',  # en mission / futur inter co
        'perimeterType': 'projects',
        'perimeterPoles': '[1]',  # pole Patrick
        'period': 'monthly',
        'order': 'asc',
        'sort': 'availability',
        'startDate': '2024-01-01',
        'endDate': '2024-12-31',
        'maxResults': '300'
    }
    #                 "narrowPerimeter": "false", 'reportingAvailability': 'asc',

    def __init__(self, api: BoondApi, pole_id: str):
        self.api = api

        if pole_id is not None : self.paramdict['perimeterPoles'] = '['+pole_id+']'
        # otherwire  there is no perimeterPoles parameter
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

    def getProdPlanResources(self) -> [ResourceEntity]:
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
        resList = self.api.getResourcesOfProductionPlan(self.paramdict)
        return resList
