import logging

from boond.boond_api import BoondApi
from boond.entity.action_entity import ActionEntity
from boond.entity.generic_entity import GenericEntity
from boond.entity.reporting_production_plans import ReportingProductionPlans
from entities.contrat_suivi import ContratSuivi
from query.actions_query import ActionsQuery


class SuiviClientMapper:

    def __init__(self, api: BoondApi):
        self.api = api
        self.logger = logging.getLogger(__name__)

        self.appl_dict = api.getApplicationDictionary()
        return

    def accept(self, res: []) -> bool:
        return True

    def map(self, prod: ReportingProductionPlans) -> [ContratSuivi]:
        resources_in_prod_plan = prod.data_of('resource')
        suivi = []
        for resource in resources_in_prod_plan:
            self.logger.debug("map : consultant is %s",
                              resource['attributes']['firstName'] + ' ' + resource['attributes']['lastName'])
            if not self.accept(resource):
                continue

            s = ContratSuivi()
            deliver_id = resource['relationships']['deliveries']['data'][0]['id']
            if (deliver_id is None):
                continue

            delivery = prod.included_of_by_type_and_id('delivery', deliver_id)
            #proj_id = delivery['relationships']['project']['data']['id']
            proj = prod.included_of_by_type_and_id('project', delivery['relationships']['project']['data']['id'])
            contact_id = proj['relationships']['contact']['data']['id']
            contact = prod.included_of_by_type_and_id('contact', proj['relationships']['contact']['data']['id'])
            #company_id = proj['relationships']['company']['data']['id']
            company = prod.included_of_by_type_and_id('company', proj['relationships']['company']['data']['id'])

            s.person = contact['attributes']['firstName'] + ' ' + contact['attributes']['lastName']
            s.contenu = proj['attributes']['reference'] + '\n' + company['attributes']['name']

            # les merger pour la presentation
            actions: [ActionEntity] = ActionsQuery(self.api).get_client_actions(contact_id)
            if len(actions) <= 0:
                suivi.append(s)
                self.logger.info("map : no actions for %s", s.person)
                continue

            first_action: ActionEntity = actions[0]
            s.date = first_action.start_date
            manager_id = first_action.data_relationships['mainManager']['data']['id']
            if ( int(manager_id) >= 0) :
                manager = first_action.included_of_by_type_and_id('resource', manager_id)
                s.qui = first_action.included_fullname(manager) if ( manager is not None) else ''

            s.typeOf = self.appl_dict.setting_action_of('contact', first_action.type_of)
            suivi.append(s)
        # end for
        return suivi
    # end
