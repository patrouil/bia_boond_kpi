

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
        return self.data.get('type', "")

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


    def merge(self, to_import) :
        # self.data_dict['data'] = self.data_dict['data']| to_import.data_dict['data']
        self.data_dict['data']['attributes'] = self.data_attributes | to_import.data_attributes
        self.data_dict['data']['relationships'] = self.data_relationships | to_import.data_relationships
        for i in to_import.included : self.included.append(i)
        # TOTO self.data_dict['included'] = self.included.append(to_import.included)
        return self