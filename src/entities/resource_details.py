
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
import datetime

from boond.entity.action_entity import ActionEntity


class ResourceDetails :
    def __init__(self):
        self.id = None
        self.url:str = None
        self.resource_name :str= None
        self.comment :str= None
        self.state = None
        self.typeOf : str= None
        self.experience :str= None
        self.competences :str= None
        self.dispo_date: str = None
        self.titre: str = None
        self.secteur = None
        self.updateDate = None
        self.last_action:ActionEntity=None
        self.last_action_date:None
        return