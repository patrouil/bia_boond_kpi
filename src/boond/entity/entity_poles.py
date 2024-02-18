from boond.entity.generic_entity import GenericEntity


class EntityPoles(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        return


    def pole_id_by_name(self, pole_name:str):
        f =  filter(
            lambda dat:  dat['attributes']['name'] == pole_name,
            self.data)
        p =  next(f, None)
        if p is not None : return p['id']
        return None