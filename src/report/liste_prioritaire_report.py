import logging

from boond.boond_api import BoondApi

from entities.report_definition import ReportDefinition
from entities.resource_details import ResourceDetails
from entities.xls_helper import XlsHelper
from mapper.liste_prioritaire_mapper import ListePrioritaireMapper
from query.candidates_query import CandidatesQuery
from query.resources_query import ResourcesQuery
from report.generic_report import GenericReport
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

'''
PRENOMS ET NOM
STATUS
PROFIL
SECTEUR
COMPETENCES CLES
ANNEES D'EXPERIENCES
Salaire
ANGLAIS
DISPO
contraintes
'''


class ListePrioritaireReport(GenericReport):

    columns_name = ['NOM',
                    'Status',
                    'PROFIL',
                    'SECTEUR',
                    'COMPETENCES',
                    'ANNEES Epx.',
                    'Dispo',
                    'Commentaire',
                    'Dernière action'
                    ]
    columns_width = [20, 18, 40, 15, 60, 10, 20, 30, 10]
    columns_header_format = ['HeaderCenterAlign', 'HeaderCenterAlign', 'HeaderCenterAlign', 'HeaderCenterAlign', 'HeaderCenterAlign', 'HeaderCenterAlign', 'HeaderCenterAlign',
                             'HeaderCenterAlign', 'HeaderCenterAlign']
    columns_data_format = ['TextDataLeftAlign', 'TextDataWrap', 'TextDataCenterAlign', 'TextDataLestAlign', 'TextDataWrap', 'TextDataCenterAlign', 'TextDataCenterAlign',
                           'TextDataWrap', 'TextDataCenterAlign']

    def __init__(self, api: BoondApi, definition: ReportDefinition):
        super().__init__(api, definition)
        self.logger = logging.Logger(__name__)
        self.chek_mandatory_parameters()

    def put_header(self, ws: Worksheet, helper : XlsHelper):
        col = 0
        for cname in self.columns_name :
            ws.set_column(col, col, width=self.columns_width[col], cell_format=helper.format_of(self.columns_data_format[col]))
            ws.write(0, col, cname, helper.format_of(self.columns_header_format[col]))
            col = col+1
        # end for
        return

    def put_data(self, ws: Worksheet, helper : XlsHelper, details : [ResourceDetails]):
        row = 1
        for res in details :
            ws.write_url(row, 0, res.url, string=res.resource_name)
            # ws.write(row, 0, res.resource_name)
            ws.write_string(row, 1, res.state + '\n'+ res.typeOf)
            ws.write_string(row, 2, res.titre)
            if res.secteur is not None : ws.write_string(row, 3, res.secteur)
            ws.write_string(row, 4, res.competences, helper.format_of(self.columns_data_format[4]))
            if ( res.experience is not None) : ws.write_string(row, 5, res.experience)
            if ( res.dispo_date is not None) : ws.write_string(row, 6, res.dispo_date, helper.format_of(self.columns_data_format[6]))
            if ( res.comment is not None) : ws.write_string(row, 7, res.comment)
            if (res.last_action is not None ): ws.write_string(row, 8, res.last_action_date)
            row = row + 1
        return

    def chek_mandatory_parameters(self) -> None:
        assert (self.report_args.flag_name is not None)
        return

    def report_xlsx(self, helper : XlsHelper) -> None:
        flagId = self.api.getApplicationFlags().flag_id_by_name(self.report_args.flag_name)

        res_query = ResourcesQuery(self.api, flagId)
        resource_list = res_query.getResources()
        mapper = ListePrioritaireMapper(self.api)
        details = []  # ResourceDetails
        for r in resource_list:
            r = res_query.fullfillResourceInfo(r)
            details.append(mapper.mapResource(r))
        #
        spread = helper.workbook
        # resource_list = sorted(resource_list, key= lambda c: c.fin)
        ws = spread.add_worksheet('Ressources Prioritaires')
        self.put_header(ws, helper)
        self.put_data(ws, helper, details)

        can_query = CandidatesQuery(self.api, flagId)
        candidate_list = can_query.getCandidates()
        mapper = ListePrioritaireMapper(self.api)
        details = []  # ResourceDetails
        for r in candidate_list:
            r = can_query.fullfillCandidateInfo(r)
            details.append(mapper.mapCandidate(r))
        #
        # resource_list = sorted(resource_list, key= lambda c: c.fin)
        ws = spread.add_worksheet('Candidats Prioritaires')
        self.put_header(ws, helper)
        self.put_data(ws, helper, details)

        return None
