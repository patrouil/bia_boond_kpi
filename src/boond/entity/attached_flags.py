from boond.entity.generic_entity import GenericEntity


class AttachedFlags(GenericEntity):
    def __init__(self, data:dict):
        super().__init__(data)
        return

    def has_flag(self, flag_name)->bool:
        f =  filter(
            lambda inc: inc['type'] == 'flag'
            and inc['attributes']['name'] == flag_name,
            self.included)
        l = next(f, None)
        return l is not None
