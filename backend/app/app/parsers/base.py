from typing import Optional

from app.parsers import MrDParser, UberParser, LoyverseParser


class Parser:

    def __init__(self):
        self.column_mapper: Optional[dict] = None
        self.column_dtype: Optional[dict] = None
        self.db_table: Optional[dict] = None

    def set_by_template(self, template: str = None):
        if not template:
            pass

        if template == 'MRDFOOD':
            self.column_mapper = MrDParser.column_mapper
            self.column_dtype: MrDParser.column_dtype
            self.db_table = MrDParser.db_table

        if template == 'UBEREATS':
            self.column_mapper = UberParser.column_mapper
            self.column_dtype: UberParser.column_dtype
            self.db_table = UberParser.db_table

        if template == 'LOYVERSE':
            self.column_mapper = LoyverseParser.column_mapper
            self.column_dtype: LoyverseParser.column_dtype
            self.db_table = LoyverseParser.db_table

        return self
