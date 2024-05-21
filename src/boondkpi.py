import datetime
import logging.config
import sys
import getopt

from entities.xls_helper import XlsHelper
from mailler import Mailler
from pptx import Presentation
from xlsxwriter import Workbook

from configuration import Configuration
from boond.boond_api import BoondApi
from boond.boond_auth import BoondAuth
from report.report_factory import ReportFactory


def build_pages(api: BoondApi, prs: Presentation):
    reports = config.get_reports
    factory = ReportFactory()
    for rd in reports:
        r = factory.reportOf(api, rd)
        if r is None:
            logger.error("Unknown report %s" % rd.name)
        else:
            r.report_pptx(prs)
    # end for
    return


def build_sheets(api: BoondApi, xls: Workbook):
    reports = config.get_reports
    factory = ReportFactory()
    helper = XlsHelper(xls)

    # define std formats
    xls.add_format({'bold': True})

    for rd in reports:
        r = factory.reportOf(api, rd)
        if r is None:
            logger.error("Unknown report %s" % rd.name)
        else:
            r.report_xlsx(helper)
    # end for
    return


def usage():
    logger.error("Usage is boondkpi.py -c config")
    logger.error("using default")
    return


def send_mail(fname: str):
    logger.info("sending email")
    m = Mailler(config.smtp, config.sender, config.sender_password)
    m.recipient(config.recipient)
    m.subject("indicateur de suivi %s" % datetime.date.today().isoformat())
    m.body("analyse du jour")
    if fname is not None:
        m.attach(fname)
    m.send()
    return


def _pptx_report(api: BoondApi, fname: str) -> None:
    prs = Presentation(config.template)
    build_pages(api, prs)
    prs.save(fname)
    return


def _xlsx_report(api: BoondApi, fname: str) -> None:
    xls = Workbook(fname)
    build_sheets(api, xls)
    xls.close()
    return


def do_report() -> int:
    auth = BoondAuth()
    auth.clientTokenAuth(config.client_token, config.user_token, config.client_key)
    api = BoondApi(auth, config.boond_host)
    # open template presentation

    fname: str = config.outdir + '/'
    try:
        fname = fname + (config.basename % datetime.date.today().isoformat())
    except:
        fname = fname + config.basename
    # end try
    if config.format == 'PPTX':
        _pptx_report(api, fname)
    if config.format == 'XLSX':
        _xlsx_report(api, fname)

    s = config.smtp
    if s is not None:
        send_mail(fname)
    return 0


if __name__ == '__main__':
    logging.config.fileConfig('conf/logging.conf')
    logger = logging.getLogger(__name__)

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "c:")
        configFileName = None
        for opt, arg in opts:
            if opt in ['-c']:
                configFileName = arg
    except Exception as ex:
        logger.error("__main__ : ex is %s", ex)
        usage()
        configFileName = None

    config = Configuration(filename=configFileName)

    sys.exit(do_report())  # next section explains the use of sys.exit
# end
