
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
        return