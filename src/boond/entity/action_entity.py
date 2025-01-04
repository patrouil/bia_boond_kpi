import html2text

from boond.entity.generic_entity import GenericEntity


class ActionEntity(GenericEntity):

    def __init__(self, data: dict):
        super().__init__(data)
        self.html_conv = html2text.HTML2Text()
        return

    @property
    def start_date(self) -> str:
        return str(self.data_attributes.get('startDate', ''))

    @property
    def creation_date(self) -> str:
        return str(self.data_attributes.get('creationDate', ''))

    @property
    def type_of(self) -> int:
        return int(self.data_attributes.get('typeOf', -1))

    @property
    def text(self) -> str:
        return str(self.data_attributes.get('text', ''))

    def text_summary(self, max_char:int = 4)-> str:
        t = self.html_conv.handle(self.text)
        t = t.replace('\n\n', '\n')
        l = t.split('\n',  max_char-1)
        t2 = '\n'.join(map(str, l[0:max_char-1]))
        return t2
