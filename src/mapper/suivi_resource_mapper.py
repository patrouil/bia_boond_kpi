import logging

from boond.boond_api import BoondApi
from boond.entity.reporting_production_plans import ReportingProductionPlans
from entities.contrat_suivi import ContratSuivi
from query.last_resources_actions_query import LastResourceActionQuery


class SuiviResourceMapper:

    def __init__(self, api:BoondApi):
        self.api = api
        self.logger = logging.getLogger(__name__)

        self.appl_dict = api.getApplicationDictionary()
        return


    def accept(self, res : [])->bool:
        return True


    def map(self, prod: ReportingProductionPlans) -> [ContratSuivi]:
        resources_en_production = prod.data_of('resource')
        suivi = []
        for resource in resources_en_production:
            self.logger.debug("map : consultant is %s", resource['attributes']['firstName'] + ' ' + resource['attributes']['lastName'])
            if not self.accept(resource) :
                continue

            s = ContratSuivi()
            deliver_id = resource['relationships']['deliveries']['data'][0]['id']
            if ( deliver_id is not None) :
                deliv = prod.included_of_by_type_and_id('delivery', deliver_id)
                proj_id = deliv['relationships']['project']['data']['id']
                proj = prod.included_of_by_type_and_id('project', proj_id)
                s.contenu = proj['attributes']['reference']
            # there can be many deliveries per resource
            # les merger pour la presentation
            s.person = resource['attributes']['firstName'] + ' ' + resource['attributes']['lastName']
            actions =  LastResourceActionQuery(self.api).get_rh_actions(resource['id'])
            if  actions.is_empty :
                self.logger.info("map : no actions for %s", s.person)
                suivi.append(s)
                continue
            d = actions.data_dict['data'][0]
            s.date = d['attributes']['startDate']
            pid = d['relationships']['mainManager']['data']['id']
            inc = actions.included_of_by_type_and_id('resource', pid)
            s.qui = inc['attributes']['firstName'] + ' ' + inc['attributes']['lastName']

            s.typeOf = self.appl_dict.setting_action_of('resource', d['attributes']['typeOf'])
            suivi.append(s)
        # end for
        return suivi
    # end
