from boond.entity.generic_entity import GenericEntity

'''
{'meta': {'version': '8.8.0.25', 'androidMinVersion': '2.24.0', 'iosMinVersion': '2.22.0', 'isLogged': True, 'language': 'fr', 'timestamp': 1715842065896, 'customer': 'groupebia'}, 
'data': [
    {'id': '2', 'type': 'flag', 
    'attributes': {'name': 'Action à relancer sous 1 mois'}, 
    'relationships': {'mainManager': 
                    {'data': {'id': '1', 'type': 'resource'}}}}, 
    {'id': '4', 'type': 'flag', 'attributes': {'name': 'Action à relancer sous 1 semaine'}, 'relationships': {'mainManager': {'data': {'id': '1', 'type': 'resource'}}}}, {'id': '5', 'type': 'flag', 'attributes': {'name': 'Action à relancer sous 3 mois'}, 'relationships': {'mainManager': {'data': {'id': '1', 'type': 'resource'}}}}, {'id': '3', 'type': 'flag', 'attributes': {'name': 'Candidat sur mission disponible immédiatement à fort potentiel'}, 'relationships': {'mainManager': {'data': {'id': '1', 'type': 'resource'}}}}, {'id': '8', 'type': 'flag', 'attributes': {'name': 'Pole Maveric Ouest'}, 'relationships': {'mainManager': {'data': {'id': '76', 'type': 'resource'}}}}, {'id': '9', 'type': 'flag', 'attributes': {'name': 'Satellite Julien'}, 'relationships': {'mainManager': {'data': {'id': '13193', 'type': 'resource'}}}}, {'id': '10', 'type': 'flag', 'attributes': {'name': 'TOP 10 Maverick Sud'}, 'relationships': {'mainManager': {'data': {'id': '32', 'type': 'resource'}}}}], 'included': [{'id': '1', 'type': 'resource', 'attributes': {'lastName': 'SAIMAN', 'firstName': 'Jonathan'}}, {'id': '76', 'type': 'resource', 'attributes': {'lastName': 'Rouillon', 'firstName': 'Patrick'}}, {'id': '13193', 'type': 'resource', 'attributes': {'lastName': 'Bourdoncle', 'firstName': 'Julien'}}, {'id': '32', 'type': 'resource', 'attributes': {'lastName': 'Battini', 'firstName': 'Olivier'}}]}

'''

class ApplicationFlags(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        return

    def flag_id_by_name(self, flag_name) -> str:
        f = filter(
            lambda inc: inc['type'] == 'flag'
                        and inc['attributes']['name'] == flag_name,
            self.data)
        l = next(f, None)
        if l is not None: return l.get('id')
        return None
# end class
