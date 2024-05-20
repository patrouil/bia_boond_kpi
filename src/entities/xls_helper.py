import logging
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Format


class XlsHelper :

    _instance = None

    # singleton pattern
    '''
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._is_ready = False
        # end if
        return cls._instance

    def __init__(self, wb: Workbook):
        if not self._is_ready:
            self.logger = logging.getLogger(self.__class__.__name__)
            self.workbook =wb
            self.format_registry = {'default' : wb.formats[0] }
        # end
        self._is_ready = True  # to avoid multiples init.
        return
'''
    def __init__(self, wb: Workbook):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.workbook = wb
        self.format_registry = {}
        self._std_formats()
        return

    def _std_formats(self)-> None:
        self.format_registry['default'] = self.workbook.formats[0]

        self.register_format('HeaderLeftAlign', self.workbook.add_format({'bold': True, 'align': 'left'}))
        self.register_format('HeaderCenterAlign', self.workbook.add_format({'bold': True, 'align': 'center'}))

        self.register_format('TextDataLeftAlign', self.workbook.add_format({'bold': False, 'align': 'left'}))

        self.register_format('TextDataCenterAlign', self.workbook.add_format({'bold': False, 'align': 'center'}))
        self.register_format('TextDataWrap', self.workbook.add_format({'bold': False, 'text_wrap': True}))

        return

    def register_format(self, name : str, fmt : Format)-> None:
        self.format_registry[name] = fmt
        return

    def format_of(self, name)-> Format:
        f = self.format_registry.get(name, self.format_registry['default'])
        return f


