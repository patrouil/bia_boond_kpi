from datetime import datetime

from dateutil import parser

'''
[{'id': '3546', 'type': 'candidate',
'attributes': {
'creationDate': '2018-10-21T16:24:23+0200',
'updateDate': '2024-05-15T12:20:58+0200',
'civility': 0, 'firstName': 'Ferhat', 'lastName': 'BENAMARA',
'state': 7,
 'typeOf': -1, 'isVisible': True, 'thumbnail': '',
  'availability': -1, 'skills': '', 'diplomas': [], 'mobilityAreas': [],
  'activityAreas': [], 'globalEvaluation': '', 'languages': [{'language': 'anglais', 'level': 'scolaire'}],
  'expertiseAreas': [], 'experience': 1, 'references': [], 'evaluations': [], 'tools': [],
   'title': 'CONSULTANT asset management', 'email1': 'ferhatbenamara87@gmail.com', 'email2': '', 'email3': '', 'phone1': '07 62 86 49 67', 'phone2': '', 'town': '', 'country': 'France', 'source': {'typeOf': 8, 'detail': ''}, 'numberOfResumes': 2, 'numberOfActivePositionings': 0, 'socialNetworks': [], 'canShowTechnicalData': True, 'canShowActions': True}, 
'relationships': {'mainManager': {'data': {'id': '2', 'type': 'resource'}}, 'agency': {'data': {'id': '2', 'type': 'agency'}}, 'pole': {'data': None}}}
]
'''


class GenericEntity:

    def __init__(self, data: dict):
        self.data_dict = data
        return

    @property
    def meta(self) -> dict:
        return self.data_dict['meta']

    @property
    def data(self) -> dict:
        return self.data_dict['data']

    @property
    def data_attributes(self) -> dict:
        return self.data['attributes']

    @property
    def data_relationships(self) -> dict:
        return self.data.get('relationships', {})

    @property
    def included(self) -> list:
        return self.data_dict.get('included', [])

    @property
    def entity_id(self) -> str:
        return self.data.get('id', '-1')

    @property
    def entity_type(self) -> str:
        return self.data.get('type', '')

    @property
    def entity_creation_date(self) -> datetime:
        d = self.data_attributes.get('creationDate', None)
        if d is not None:
            return parser.parse(d)
        else:
            return None

    @property
    def entity_update_date(self) -> datetime:
        d = self.data_attributes.get('updateDate', None)
        if d is not None:
            return parser.parse(d)
        else:
            return None

    @property
    def entity_id(self) -> str:
        return self.data.get('id', '-1')

    @property
    def is_empty(self) -> bool:
        if self.data_dict is None: return True
        if (len(self.data) <= 0): return True
        return False

    def included_of_by_type_and_id(self, selType: str, uid: str):
        f = filter(
            lambda inc: inc['type'] == selType and inc['id'] == uid,
            self.included)
        return next(f, None)

    def all_included_of_by_type_and_id(self, selType: str, uid: str):
        f = filter(
            lambda inc: inc['type'] == selType and inc['id'] == uid,
            self.included)
        return list(f)

    def included_fullname(self, included_dict: {}) -> str:
        attr = included_dict['attributes']
        return attr['firstName'] + ' ' + attr['lastName'] \
            if (attr is not None) else ''

    def merge(self, to_import):
        # self.data_dict['data'] = self.data_dict['data']| to_import.data_dict['data']
        self.data_dict['data']['attributes'] = self.data_attributes | to_import.data_attributes
        self.data_dict['data']['relationships'] = self.data_relationships | to_import.data_relationships
        for i in to_import.included: self.included.append(i)
        # TOTO self.data_dict['included'] = self.included.append(to_import.included)
        return self
