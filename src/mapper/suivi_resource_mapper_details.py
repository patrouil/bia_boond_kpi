import logging

from boond.boond_api import BoondApi
from boond.entity.action_entity import ActionEntity
from boond.entity.resource_entity import ResourceEntity
from entities.contrat_suivi import ContratSuivi
from query.last_resources_actions_query import LastResourceActionQuery

class SuiviResourceMapperDetails:

    def __init__(self, api: BoondApi):
        self.api = api
        self.logger = logging.getLogger(__name__)

        self.appl_dict = api.getApplicationDictionary()
        return


    def accept(self, res : [])->bool:
        return True

    def map(self, prod: [ResourceEntity]) -> [ContratSuivi]:
        suivi = []
        resource : ResourceEntity
        for resource in prod:
            self.logger.debug("map : consultant is %s", resource.full_name )
            if not self.accept(resource) :
                continue

            s = ContratSuivi()
            deliver_id = resource.data_relationships['deliveries']['data'][0]['id']
            if ( deliver_id is not None) :
                deliv = resource.included_of_by_type_and_id('delivery', deliver_id)
                proj_id = deliv['relationships']['project']['data']['id']
                proj = resource.included_of_by_type_and_id('project', proj_id)
                s.contenu = proj['attributes']['reference']
            # there can be many deliveries per resource
            # les merger pour la presentation
            s.person = resource.full_name
            actions : [ActionEntity]
            actions = LastResourceActionQuery(self.api).get_any_actions(resource.entity_id)
            if  len(actions) <= 0  :
                self.logger.info("map : no actions for %s", s.person)
                suivi.append(s)
                continue
            d : ActionEntity = actions[0]
            s.date = d.start_date
            pid = d.data_relationships['mainManager']['data']['id']
            inc = d.included_of_by_type_and_id('resource', pid)
            s.qui = inc['attributes']['firstName'] + ' ' + inc['attributes']['lastName']
            s.typeOf = self.appl_dict.setting_action_of('resource', str(d.type_of))
            if ( s.typeOf is None) : s.typeOf = ''
            s.actionText = d.text_summary()
            suivi.append(s)
        # end for
        return suivi
    # end
