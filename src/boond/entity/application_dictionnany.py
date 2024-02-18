from boond.entity.generic_entity import GenericEntity


class ApplicationDictionary(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        return

    @property
    def setting(self) -> list:
        return self.data['setting']

    def setting_action_of(self, entity_name: str, action_id: str) -> str:
        f = filter(
            lambda inc: inc['id'] == action_id,
            self.setting['action'][entity_name])
        l = next(f, None)
        if (l is None): return None
        return l['value']
