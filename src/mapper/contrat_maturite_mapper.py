import logging

from boond.boond_api import BoondApi
from boond.entity.reporting_production_plans import ReportingProductionPlans
from entities.maturite_contrat import MaturiteContrat


class MaturiteContratMapper:
    def __init__(self, api: BoondApi):
        self.logger = logging.getLogger(__name__)
        self.api = api
        return

    def minStr(self, s1, s2)->str:
        if ( s2 is None or s2 == '' ):return s1
        if ( s1 is not None and s1 != '' and s1 < s2) : return s1
        return s2

    def maxStr(self, s1, s2)->str:
        if ( s1 is None or s1 == ''): return s2
        if ( s2 is not None and s2 != '' and s1 < s2) : return s2
        return s1

    def accept(self, res : [])->bool:
        return True
#        id = res['id']
 #       flags = self.api.getResourceFlagsById(id)
  #      if ( flags.is_empty()): return False
   #     return flags.has_flag('Pole Maveric Ouest')

    def map(self, prod: ReportingProductionPlans) -> [MaturiteContrat]:
        res = prod.data_of('resource')
        maturities = []
        for r in res:
            self.logger.debug("map : consultant is %s", r['attributes']['firstName'] + ' ' + r['attributes']['lastName'])
            if not self.accept(r) :
                continue
            self.logger.debug("map : consultant accepted")

        # there can be many deliveries per resource
            # les merger pour la presentation
            m = MaturiteContrat()
            m.consultant = r['attributes']['firstName'] + ' ' + r['attributes']['lastName']

            for d in prod.resource_deliveries(r) :
                deliv = prod.included_of_by_type_and_id('delivery', d['id'])
                m.debut = self.minStr(m.debut,deliv['attributes']['startDate'])
                m.fin = self.maxStr(m.fin, deliv['attributes']['endDate'])
                self.logger.debug("map : deliveries %s - %s", deliv['attributes']['startDate'], deliv['attributes']['endDate'])

                proj_id = deliv['relationships']['project']['data']['id']
                proj = prod.included_of_by_type_and_id('project', proj_id)
                if ( m.reference == ''): m.reference = proj['attributes']['reference']
                contact_id = proj['relationships']['contact']['data']['id']
                company_id = proj['relationships']['company']['data']['id']

                contact = prod.included_of_by_type_and_id('contact', contact_id)
                company = prod.included_of_by_type_and_id('company', company_id)
                if ( m.donneurOrdre == '') : m.donneurOrdre = contact['attributes']['firstName'] + ' ' + contact['attributes']['lastName']
                if ( m.client == '') : m.client = company['attributes']['name']
            # end for
            maturities.append(m)
    # end for
        return maturities
    # end
