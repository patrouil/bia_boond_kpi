class EntityActions:

    def __init__(self, data: dict):
        self.data_dict = data
        return

    @property
    def data(self) -> list:
        return self.data_dict['data']

    def is_empty(self) -> bool:
        if (self.data_dict is None): return True
        if (len(self.data_dict['data']) <= 0): return True
        return False


    def included_of(self, selType, uid)-> list:
        f =  filter(
            lambda inc: inc['type'] == selType  and inc['id'] == uid,
            self.data_dict['included'])
        l = list(f)
        return l[0]
