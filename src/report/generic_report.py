from typing import Any

from pptx.text.text import TextFrame
from pptx.util import Pt
from pptx import Presentation
from xlsxwriter import Workbook

from boond.boond_api import BoondApi
from entities.report_definition import ReportDefinition
from entities.xls_helper import XlsHelper


class GenericReport:

    def __init__(self, api: BoondApi, definition : ReportDefinition):
        self.api = api
        self.report_args = definition
        return

    def report_pptx(self, presentation : Presentation):
        pass

    def report_xlsx(self, helper : XlsHelper):
        pass

    def put_text(self, tf: TextFrame, t: str) -> None:
        p = tf.paragraphs[0]
        p.clear()
        r = p.add_run()
        r.font.size = Pt(12)
        r.text = t
        return None

    def array_writer(self, prs : Presentation , obj_list: [Any], write_func: Any, row_per_page:int):
        row = 0
        while row < len(obj_list) :
            j = min(len(obj_list) , row+ row_per_page)
            write_func(obj_list[row: j], prs)
            row = row+row_per_page
        return
    #
