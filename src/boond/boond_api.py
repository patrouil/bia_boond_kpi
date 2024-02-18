import http
import json
import logging
import urllib.parse
from http.client import HTTPConnection
from typing import Any

from boond.entity.attached_flags import AttachedFlags
from boond.entity.entity_actions import EntityActions
from boond.boond_auth import BoondAuth
from boond.entity.reporting_production_plans import ReportingProductionPlans
from boond.entity.application_dictionnany import ApplicationDictionary
from boond.entity.entity_poles import EntityPoles


# narrowPerimeter=false&occupationGradient=false&perimeterPoles=%5B%224%22%5D&perimeterType=projects&period=periodDynamic&periodDynamic=thisMonth&positioningPeriod=created&regroup=false&saveSearch=true&showContracts=false
# Boond APi documentation https://doc.boondmanager.com/api-externe/


class BoondApi:
    URL_CURRENT_USER = '/api/application/current-user'
    URL_PRODUCTION_PLAN = '/api/reporting-production-plans'
    URL_RESOURCES_ATTACHED_FLAG = "/api/resources/%s/attached-flags"
    URL_RESOURCES_ACTIONS       = "/api/resources/%s/actions"
    URL_CONTACTS_ACTIONS        = "/api/contacts/%s/actions"
    URL_APPLICATION_DICTIONARY  = '/api/application/dictionary'
    URL_POLES                   = '/api/poles'

    def __init__(self, auth: BoondAuth, host: str) -> None:
        self.logger = logging.getLogger(__name__)
        self.auth = auth
        self.host = host
        return

    def buildUrl(self, baseUrl: str, args: dict) -> str:
        u = baseUrl
        if (args is not None):
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
            l = resp.headers.get('Location', None)
            self.logger.error("get: %d - %s", resp.status, resp.reason)
            self.logger.error("get: location %s", l)
        conn.close()
        return None

    def getReportingProductionPlan(self, args) -> ReportingProductionPlans:
        s = self.buildUrl(self.URL_PRODUCTION_PLAN, args)
        val = self.get(s)
        assert (val is not None)
        # self.logger.debug("getReportingProductionPlan: %s", val)

        return ReportingProductionPlans(val)

    def getApplicationDictionary(self) -> ApplicationDictionary:
        val = self.get(self.URL_APPLICATION_DICTIONARY)
        assert (val is not None)
        # self.logger.debug("getApplicationDictionary: %s", val)

        return ApplicationDictionary(val)

    def getPoles(self) -> EntityPoles:
        val = self.get(self.URL_POLES)
        assert (val is not None)
        self.logger.debug("getPoles: %s", val)

        return EntityPoles(val)

    def getResourceFlagsById(self, id: str) -> AttachedFlags:
        s = self.URL_RESOURCES_ATTACHED_FLAG % id
        val = self.get(s)
        assert (val is not None)
        # self.logger.debug("getResourceFlagsById: %s",val)

        return AttachedFlags(val)

    def getResourceActionsById(self, id: str, args) -> EntityActions:
        s = self.buildUrl(self.URL_RESOURCES_ACTIONS % id, args)
        val = self.get(s)
        assert (val is not None)

        return EntityActions(val)

    def getContactActionsById(self, id: str, args) -> EntityActions:
        s = self.buildUrl(self.URL_CONTACTS_ACTIONS % id, args)
        val = self.get(s)
        assert (val is not None)

        return EntityActions(val)
# end
