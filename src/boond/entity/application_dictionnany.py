class ApplicationDictionary:

    def __init__(self, data: dict):
        self.data_dict = data
        return

    @property
    def data(self) -> list:
        return self.data_dict['data']

    @property
    def setting(self) -> list:
        return self.data_dict['data']['setting']

    def setting_action_of(self, entity_name: str, action_id: str) -> str:
        f = filter(
            lambda inc: inc['id'] == action_id,
            self.setting['action'][entity_name])
        l = list(f)
        if (len(l) <= 0): return None
        return l[0]['value']
