class GenericEntity:

    def __init__(self, data: dict):
        self.data_dict = data
        return

    @property
    def meta(self) -> list:
        return self.data_dict['meta']

    @property
    def data(self) -> list:
        return self.data_dict['data']

    @property
    def included(self) -> list:
        return self.data_dict['included']

    def is_empty(self) -> bool:
        if (self.data_dict is None): return True
        if (len(self.data) <= 0): return True
        return False

    def included_of_by_type_and_id(self, selType: str, uid: str):
        f = filter(
            lambda inc: inc['type'] == selType and inc['id'] == uid,
            self.included)
        return next(f, None)

