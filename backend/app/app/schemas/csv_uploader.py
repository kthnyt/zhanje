from pydantic import BaseModel


class CsvUploaderCreate(BaseModel):
    template: str
