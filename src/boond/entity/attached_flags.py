

class AttachedFlags:
    def __init__(self, data:dict):
        self.data_dict = data
        return

    @property
    def data(self)-> list:
        return self.data_dict['data']

    def has_flag(self, flag_name)->bool:
        f =  filter(
            lambda inc: inc['type'] == 'flag'
            and inc['attributes']['name'] == flag_name,
            self.data_dict['included'])
        l = list(f)
        return len(l) > 0

    def is_empty(self)->bool:
        if ( self.data_dict is None): return True
        if ( len(self.data_dict['data']) <= 0 ): return True
        return False