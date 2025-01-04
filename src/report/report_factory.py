from boond.boond_api import BoondApi
from entities.report_definition import ReportDefinition
from report.contrat_client_suivi_engine import ContratClientSuiviEngine
from report.contrat_maturity_engine import ContratMaturityEngine
from report.contrat_resource_suivi_engine import ContratResourceSuiviEngine
from report.contrat_resource_suivi_details import ContratResourceSuiviDetails
from report.generic_report import GenericReport
from report.liste_prioritaire_report import ListePrioritaireReport

class ReportFactory :

    SUIVI_MISSION = 'suivi-mission'
    SUIVI_CLIENT = 'suivi-client'
    SUIVI_RESOURCE = 'suivi-consultant'
    SUIVI_RESOURCE_ACTION = 'suivi-consultant-action'
    LISTE_PRIORITAIRE = "liste-prioritaire"

    def __init__(self):
        pass

    def reportOf(self,  api: BoondApi, definition: ReportDefinition)-> GenericReport:

        if ( definition.name == self.SUIVI_MISSION): return ContratMaturityEngine(api, definition)
        if ( definition.name == self.SUIVI_CLIENT) : return ContratClientSuiviEngine(api, definition)
        if ( definition.name == self.SUIVI_RESOURCE) : return ContratResourceSuiviEngine(api, definition)
        if ( definition.name == self.LISTE_PRIORITAIRE) : return ListePrioritaireReport(api, definition)
        if ( definition.name == self.SUIVI_RESOURCE_ACTION) : return ContratResourceSuiviDetails(api, definition)

    #end class
