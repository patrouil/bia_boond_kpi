from boond.entity.generic_entity import GenericEntity

'''
 {'id': '10913', 'type': 'resource', 
    'attributes': {
        'canShowTechnicalData': True, 
        'canShowActions': True, 'civility': 0, 
        'firstName': 'Céline', 'lastName': 'XXXXX', 
        'creationDate': '2019-11-20T17:15:06+0100', 
        'updateDate': '2024-05-07T14:21:06+0200', 'typeOf': 0,
         'state': 5, 'isVisible': True, 
         'thumbnail': '', 'skills': '',
          'mobilityAreas': [], 
          'title': 'CHEF DE PROJET', 
          'availability': '2025-01-01',
           'realAvailability': '2025-01-01', 'averageDailyPriceExcludingTax': 0, 
           'email1': 'celine.douaud@gmail.com', 'email2': 'celine.douaud@alteam.com', 'email3': 'celine.douaud@externe.bnpparibas.com', 
           'phone1': '0607252820', 'phone2': '', 'currency': 0,
            'exchangeRate': 1, 'currencyAgency': 0, 'exchangeRateAgency': 1, 
            'numberOfResumes': 2,
             'numberOfActivePositionings': 1, 'tools': [],
              'expertiseAreas': [], 'activityAreas': [], 
              'diplomas': ['DEA - UNIVERSITE', 'Maitrise - Mathématique Appliquée et Sciences Sociales - UNIVERSITE', 'Baccalauréat - UNIVERSITE'], 
              'experience': -1, 
              'references': [{'id': '2811', 'title': 'TRADER - CIC LYONNAISE DE BANQUE - 01/08/1996 - 01/02/2002', 'description': 'o FX OTC et Spot Trader\r\n'}, {'id': '2812', 'title': 'PRODUCT MANAGER KONDOR + - THOMSON REUTERS - 01/06/2007 - 01/07/2008', 'description': "* Responsable de la Roadmap Kondor + o Participation et animation de nombreux évènements clients afin de recueillir les besoins et de construire la vision stratégique à long terme o Gestion du budget de développement et définition des priorités fonctionnelles et techniques de développement o Evangélisation et formation des équipes d'avant-vente sur les nouvelles fonctionnalités 5\r\n"}], 
              'languages': []}, 
              'relationships': {
                    'mainManager': {'data': {'id': '14248', 'type': 'resource'}}, 
                    'hrManager': {'data': {'id': '9791', 'type': 'resource'}}, 
                    'agency': {'data': {'id': '3', 'type': 'agency'}}, 
                    'pole': {'data': {'id': '4', 'type': 'pole'}}}
            },
             
'''


class ResourceEntity(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        return

    @property
    def full_name(self) -> str:
        return "%s %s" % (self.data_attributes.get('firstName', ''), self.data_attributes.get('lastName', ''))

    @property
    def availability(self) -> str:
        return str(self.data_attributes.get('availability', ''))

    @property
    def skills(self) -> str:
        return self.data_attributes.get('skills', None)

    @property
    def title(self) -> str:
        return self.data_attributes.get('title', None)

    @property
    def state(self) -> str:
        return self.data_attributes.get('state', None)

    @property
    def extertiseAreas(self) -> [str]:
        return self.data_attributes.get('expertiseAreas', [])

    @property
    def experience(self) -> [str]:
        return self.data_attributes.get('experience', '-1')

    @property
    def informationComments(self) -> str:
        return self.data_attributes.get('informationComments', '')

    @property
    def typeOf(self) -> str:
        return str(self.data_attributes.get('typeOf', "-1"))
