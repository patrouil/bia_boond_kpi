import datetime
import logging.config
import sys

from configuration import Configuration
from engine.contrat_client_suivi_engine import ContratClientSuiviEngine
from engine.contrat_maturity_engine import ContratMaturityEngine
from engine.contrat_resource_suivi_engine import ContratResourceSuiviEngine

from boond.boond_api import BoondApi
from boond.boond_auth import BoondAuth
from pptx import Presentation

from mailler import Mailler


def maturityKpi(api:BoondApi, prs : Presentation):
    ContratMaturityEngine(api).projectMaturiteKPI(prs)

    ContratResourceSuiviEngine(api).projectSuiviKPI(prs)
    ContratClientSuiviEngine(api).projectSuiviKPI(prs)

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

def main() -> int:
    auth = BoondAuth()
    auth.clientTokenAuth(config.client_token, config.user_token, config.client_key)
    api = BoondApi(auth, config.boond_host)
    # open template presantion
    prs = Presentation(config.template)
    maturityKpi(api, prs)
    fname = config.outdir + '/'+ (config.basename % datetime.date.today().isoformat())
    prs.save(fname)

    s = config.smtp
    if ( s is not None):
        send_mail(fname)
    return 0

if __name__ == '__main__':
    logging.config.fileConfig('conf/logging.conf')
    logger = logging.getLogger(__name__)
    config = Configuration()
    sys.exit(main())  # next section explains the use of sys.exit
# end
