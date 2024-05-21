from boond.entity.generic_entity import GenericEntity

'''
[{'id': '3546', 'type': 'candidate', 
'attributes': {'creationDate': '2018-10-21T16:24:23+0200', 
'updateDate': '2024-05-15T12:20:58+0200', 
'civility': 0, 'firstName': 'Ferhat', 'lastName': 'BENAMARA', 
'state': 7,
 'typeOf': -1, 'isVisible': True, 'thumbnail': '',
  'availability': -1, 'skills': '', 'diplomas': [], 'mobilityAreas': [], 
  'activityAreas': [], 'globalEvaluation': '', 'languages': [{'language': 'anglais', 'level': 'scolaire'}], 
  'expertiseAreas': [], 'experience': 1, 'references': [], 'evaluations': [], 'tools': [],
   'title': 'CONSULTANT asset management', 'email1': 'ferhatbenamara87@gmail.com', 'email2': '', 'email3': '', 'phone1': '07 62 86 49 67', 'phone2': '', 'town': '', 'country': 'France', 'source': {'typeOf': 8, 'detail': ''}, 'numberOfResumes': 2, 'numberOfActivePositionings': 0, 'socialNetworks': [], 'canShowTechnicalData': True, 'canShowActions': True}, 'relationships': {'mainManager': {'data': {'id': '2', 'type': 'resource'}}, 'agency': {'data': {'id': '2', 'type': 'agency'}}, 'pole': {'data': None}}}]             
'''


class CandidateEntity(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        return

    @property
    def full_name(self)-> str:
        return "%s %s" % (self.data_attributes.get('firstName', ''), self.data_attributes.get('lastName', ''))

    @property
    def availability(self)-> str:
        return str(self.data_attributes.get('availability', ''))

    @property
    def skills(self)-> str:
        return self.data_attributes.get('skills', None)

    @property
    def title(self)-> str:
        return self.data_attributes.get('title', None)

    @property
    def state(self)-> str:
        return self.data_attributes.get('state', None)

    @property
    def extertiseAreas(self)-> [str]:
        return self.data_attributes.get('expertiseAreas', [])

    @property
    def experience(self)-> [str]:
        return self.data_attributes.get('experience', '-1')

    @property
    def informationComments(self)-> str:
        return self.data_attributes.get('informationComments', '')

    @property
    def typeOf(self)-> str:
        return str(self.data_attributes.get('typeOf', '-1'))