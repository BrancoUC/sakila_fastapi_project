# entities/language.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Language(BaseModel):
    language_id: int
    name: str
    last_update: Optional[datetime] = None

class LanguageCreate(BaseModel):
    name: str
