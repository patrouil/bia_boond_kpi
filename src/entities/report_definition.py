

class ReportDefinition:

    def __init__(self, name: str, definition : dict):
        self.name = name
        self.definition = definition
        return

    @property
    def flag_name(self)-> str:
        return self.definition.get('flag_name', None)

    @property
    def pole_id(self)-> str:
        return self.definition.get('pole_id', None)

    # end class
