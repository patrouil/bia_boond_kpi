import logging
from datetime import date

from boond.boond_api import BoondApi
from boond.entity.candidate_entity import CandidateEntity
from boond.entity.resource_entity import ResourceEntity
from entities.resource_details import ResourceDetails
from query.actions_query import ActionsQuery


class ListePrioritaireMapper:

    def __init__(self, api: BoondApi):
        self.api = api
        self.logger = logging.getLogger(__name__)

        self.appl_dict = api.getApplicationDictionary()
        self.action_query = ActionsQuery(api)
        return

    def accept(self, res: []) -> bool:
        return True

    def mapResource(self, res: ResourceEntity) -> ResourceDetails:
        res_det = ResourceDetails()
        res_det.id = res.entity_id
        res_det.url = "https://ui.boondmanager.com/resources/%s/overview" % res.entity_id
        res_det.resource_name = res.full_name
        res_det.competences = res.skills
        theDate= date.fromisoformat(res.availability)  if res.availability is not None else date.fromisoformat('9999-12-31')
        res_det.dispo_date = theDate.strftime('%d/%m/%Y') if theDate is not None else ''
        res_det.experience = self.appl_dict.setting_experience_of(res.experience) if not res.experience == '-1' else ''
        res_det.state = self.appl_dict.setting_state_of('resource', res.state) if res.state is not None else ''
        res_det.typeOf = self.appl_dict.setting_type_of('resource', int(res.typeOf)) if not res.typeOf == '-1' else ''
        res_det.titre = res.title
        for e in res.extertiseAreas: res_det.secteur = "%s, %s" % (
        res_det.secteur, e) if res_det.secteur is not None else e
        res_det.comment = res.informationComments
        res_det.updateDate = res.entity_update_date
        return res_det

    def mapCandidate(self, can: CandidateEntity) -> ResourceDetails:
        res_det = ResourceDetails()
        res_det.id = can.entity_id
        res_det.url = "https://ui.boondmanager.com/candidates/%s/overview" % can.entity_id
        res_det.resource_name = can.full_name
        res_det.competences = can.skills
        res_det.dispo_date = self.appl_dict.setting_availability_of(
            int(can.availability)) if not can.availability == -1 else ''
        res_det.experience = self.appl_dict.setting_experience_of(can.experience) if not can.experience == '-1' else ''
        res_det.state = self.appl_dict.setting_state_of('candidate', can.state) if can.state is not None else ''
        res_det.typeOf = self.appl_dict.setting_type_of('resource', int(can.typeOf)) if not can.typeOf == '-1' else ''
        res_det.titre = can.title
        for e in can.extertiseAreas: res_det.secteur = "%s, %s" % (
        res_det.secteur, e) if res_det.secteur is not None else e
        res_det.comment = can.informationComments
        res_det.updateDate = can.entity_update_date
        can_act = self.action_query.get_candidate_actions(res_det.id)
        if len(can_act) > 0 :
            res_det.last_action = can_act[0]
            theDate= date.fromisoformat(res_det.last_action.start_date[:10]) if res_det.last_action is not None else None
            res_det.last_action_date = theDate.strftime('%d/%m/%Y') if theDate is not None else ''
        return res_det
