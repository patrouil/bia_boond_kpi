import http
import json
import logging
import urllib.parse
from http.client import HTTPConnection
from typing import Any

from boond.entity.action_entity import ActionEntity
from boond.entity.application_flags import ApplicationFlags
from boond.entity.attached_flags import AttachedFlags
from boond.entity.candidate_entity import CandidateEntity
from boond.entity.entity_actions import EntityActions
from boond.boond_auth import BoondAuth
from boond.entity.entity_contacts import EntityContacts
from boond.entity.reporting_production_plans import ReportingProductionPlans
from boond.entity.application_dictionnany import ApplicationDictionary
from boond.entity.entity_poles import EntityPoles
from boond.entity.resource_entity import ResourceEntity


# narrowPerimeter=false&occupationGradient=false&perimeterPoles=%5B%224%22%5D&perimeterType=projects&period=periodDynamic&periodDynamic=thisMonth&positioningPeriod=created&regroup=false&saveSearch=true&showContracts=false
# Boond APi documentation https://doc.boondmanager.com/api-externe/


class BoondApi:
    URL_CURRENT_USER = '/api/application/current-user'
    URL_PRODUCTION_PLAN = '/api/reporting-production-plans'
    URL_RESOURCES_ATTACHED_FLAG = "/api/resources/%s/attached-flags"
    URL_RESOURCES_ACTIONS       = "/api/resources/%s/actions"
    URL_CONTACTS_ACTIONS        = "/api/contacts/%s/actions"
    URL_APPLICATION_DICTIONARY  = '/api/application/dictionary'
    URL_APPLICATION_FLAGS       = '/api/application/flags'
    URL_POLES                   = '/api/poles'
    URL_CONTACTS                = '/api/contacts'
    URL_RESOURCES               = '/api/resources'
    URL_RESOURCES_DT          = '/api/resources/%s/technical-data'
    URL_RESOURCES_INFO          = '/api/resources/%s/information'
    URL_CANDIDATES               = '/api/candidates'
    URL_CANDIDATES_INFO          = '/api/candidates/%s/information'
    URL_CANDIDATES_DT          = '/api/candidates/%s/technical-data'

    def __init__(self, auth: BoondAuth, host: str) -> None:
        self.logger = logging.getLogger(__name__)
        self.auth = auth
        self.host = host
        return

    def build_url(self, baseUrl: str, args: dict = {}) -> str:
        u = baseUrl
        if args is not None:
            a = urllib.parse.urlencode(args)
            u = u + '?' + a
        return u

    def get(self, url: str) -> Any:
        conn = http.client.HTTPSConnection(self.host)
        conn.request("GET", url, None, self.auth.auth_headers)

        resp = conn.getresponse()
        if resp.status == http.client.OK:
            body = resp.read()
            # self.logger.debug("get: body is : %s",resp.reason)
            d = json.loads(body)
            conn.close()
            return d
        else:
            loc = resp.headers.get('Location', None)
            self.logger.error("get: %d - %s", resp.status, resp.reason)
            self.logger.error("get: location %s", loc)
        conn.close()
        return None

    def getReportingProductionPlan(self, args) -> ReportingProductionPlans:
        s = self.build_url(self.URL_PRODUCTION_PLAN, args)
        val = self.get(s)
        assert (val is not None)
        # self.logger.debug("getReportingProductionPlan: %s", val)

        return ReportingProductionPlans(val)


    def getResourcesOfProductionPlan(self, args) -> [ResourceEntity]:
        s = self.build_url(self.URL_PRODUCTION_PLAN, args)
        val = self.get(s)
        assert (val is not None)
        # self.logger.debug("getReportingProductionPlan: %s", val)
        return list(map(lambda ent: ResourceEntity({'meta': val['meta'], 'data':ent, 'included': val['included']} ),
                   val['data']))
        # return ReportingProductionPlans(val)


    def getApplicationDictionary(self) -> ApplicationDictionary:
        val = self.get(self.URL_APPLICATION_DICTIONARY)
        assert (val is not None)
        # self.logger.debug("getApplicationDictionary: %s", val)

        return ApplicationDictionary(val)

    def getApplicationFlags(self) -> ApplicationFlags:
        val = self.get(self.URL_APPLICATION_FLAGS)
        assert (val is not None)
        # self.logger.debug("getApplicationDictionary: %s", val)
        return ApplicationFlags(val)

    def getPoles(self) -> EntityPoles:
        val = self.get(self.URL_POLES)
        assert (val is not None)
        self.logger.debug("getPoles: %s", val)

        return EntityPoles(val)

    def getResourceFlagsById(self, id_entity: str) -> AttachedFlags:
        s = self.URL_RESOURCES_ATTACHED_FLAG % id_entity
        val = self.get(s)
        assert (val is not None)
        # self.logger.debug("getResourceFlagsById: %s",val)

        return AttachedFlags(val)

    def getResourceActionsById(self, id_entity: str, args) -> EntityActions:
        s = self.build_url(self.URL_RESOURCES_ACTIONS % id_entity, args)
        val = self.get(s)
        assert (val is not None)

        return EntityActions(val)

    def getResourceActionListById(self, id_entity: str, args) -> [ActionEntity]:
        s = self.build_url(self.URL_RESOURCES_ACTIONS % id_entity, args)
        val = self.get(s)
        assert (val is not None)

        return list(map(lambda ent: ActionEntity({'meta': val['meta'], 'data':ent, 'included': val['included']} ),
                   val['data']))

    def getContactActionsById(self, id_entity: str, args) -> EntityActions:
        s = self.build_url(self.URL_CONTACTS_ACTIONS % id_entity, args)
        val = self.get(s)
        assert (val is not None)

        return EntityActions(val)

    def getContacts(self, args) -> EntityContacts:
        s = self.build_url(self.URL_CONTACTS, args)
        val = self.get(s)
        assert (val is not None)

        return EntityContacts(val)

    def getResources(self, args) -> [ResourceEntity]:
        s = self.build_url(self.URL_RESOURCES, args)
        val = self.get(s)
        assert (val is not None)
        return list(map(lambda ent: ResourceEntity({'meta': val['meta'], 'data':ent, 'included': val['included']} ),
                    val['data']))

    def getResourceInfo(self, id_entity:str) -> ResourceEntity:
        s = self.build_url(self.URL_RESOURCES_INFO % id_entity)
        val = self.get(s)
        assert (val is not None)
        return ResourceEntity(val)

    def getResourceDT(self, id_entity:str) -> ResourceEntity:
        s = self.build_url(self.URL_RESOURCES_DT % id_entity)
        val = self.get(s)
        assert (val is not None)
        return ResourceEntity(val)

    def getCandidates(self, args) -> [CandidateEntity]:
        s = self.build_url(self.URL_CANDIDATES, args)
        val = self.get(s)
        assert (val is not None)
        return list(map( lambda ent: CandidateEntity(  {'meta': val['meta'], 'data':ent, 'included': val['included'] } ),
                    val['data']))

    def getCandidateInfo(self, id_entity:str) -> CandidateEntity:
        s = self.build_url(self.URL_CANDIDATES_INFO % id_entity)
        val = self.get(s)
        assert (val is not None)
        return CandidateEntity(val)

    def getCandidateDT(self, id_entity:str) -> CandidateEntity:
        s = self.build_url(self.URL_CANDIDATES_DT % id_entity)
        val = self.get(s)
        assert (val is not None)
        return CandidateEntity(val)
# end
