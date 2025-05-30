from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Category(BaseModel):
    category_id: Optional[int]
    name: str
    last_update: Optional[datetime]
