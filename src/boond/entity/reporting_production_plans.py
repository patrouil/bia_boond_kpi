

class ReportingProductionPlans:

    def __init__(self, data:dict):
        self.data_dict = data
        return

    @property
    def data(self)-> list:
        return self.data_dict['data']

    def included_of(self, selType)-> list:
        f =  filter(
                lambda inc: inc['type'] == selType ,
                self.data_dict['included'])
        l = list(f)
        return l

    def data_of(self, selType)->list:
        f =  filter(
            lambda inc: inc['type'] == selType ,
            self.data_dict['data'])
        l = list(f)
        return l

    def resource_deliveries(self, resource)->[]:
        r = resource['relationships']
        d = r['deliveries']
        assert(d is not None)
        return d['data']

    def included_of(self, selType, uid)-> list:
        f =  filter(
            lambda inc: inc['type'] == selType  and inc['id'] == uid,
            self.data_dict['included'])
        l = list(f)
        return l[0]

    #end
