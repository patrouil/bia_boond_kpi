import datetime
import logging.config
import sys
import getopt

from configuration import Configuration
from engine.contrat_client_suivi_engine import ContratClientSuiviEngine
from engine.contrat_maturity_engine import ContratMaturityEngine
from engine.contrat_resource_suivi_engine import ContratResourceSuiviEngine

from boond.boond_api import BoondApi
from boond.boond_auth import BoondAuth
from pptx import Presentation

from mailler import Mailler


def build_pages(api:BoondApi, prs : Presentation):
    ContratMaturityEngine(api).projectMaturiteKPI(prs, config.pole_id)

    ContratResourceSuiviEngine(api).projectSuiviKPI(prs)
    ContratClientSuiviEngine(api).projectSuiviKPI(prs)

    return

def usage():
    logger.error("Usage is boondkpi.py -c config")
    logger.error("using default")
    return

def send_mail(fname:str):
    logger.info("sending email")
    m = Mailler(config.smtp,config.sender, config.sender_password)
    m.recipient(config.recipient)
    m.subject("indicateur de suivi %s" % datetime.date.today().isoformat())
    m.body("analyse du jour")
    if ( fname is not None):
        m.attach(fname)
    m.send()
    return

def do_report() -> int:
    auth = BoondAuth()
    auth.clientTokenAuth(config.client_token, config.user_token, config.client_key)
    api = BoondApi(auth, config.boond_host)
    # open template presentation
    prs = Presentation(config.template)
    build_pages(api, prs)
    fname = config.outdir + '/'+ (config.basename % datetime.date.today().isoformat())
    prs.save(fname)

    s = config.smtp
    if ( s is not None):
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
