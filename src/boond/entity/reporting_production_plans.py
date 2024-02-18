from boond.entity.generic_entity import GenericEntity


class ReportingProductionPlans(GenericEntity):

    def __init__(self, data:dict):
        super().__init__(data)
        return


    def data_of(self, selType)->list:
        f =  filter(
            lambda inc: inc['type'] == selType ,
            self.data)
        l = list(f)
        return l

    def resource_deliveries(self, resource)->[]:
        r = resource['relationships']
        d = r['deliveries']
        assert(d is not None)
        return d['data']


    #end
