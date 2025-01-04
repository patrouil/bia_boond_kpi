from boond.entity.generic_entity import GenericEntity
from boond.entity.resource_entity import ResourceEntity


class ReportingProductionPlans(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        return

    def data_of(self, selType) -> list:
        f = filter(
            lambda inc: inc['type'] == selType,
            self.data)
        l = list(f)
        return l

    def resource_deliveries(self, resource) -> []:
        r = resource['relationships']
        d = r['deliveries']
        assert (d is not None)
        return d['data']

    def data_resources(self)-> [ResourceEntity]:
        return map( lambda ent: ResourceEntity(  {'meta': self.data_dict['meta'], 'data':ent, 'included': self.data_dict['included'] } ),
                    self.data)

    # end
