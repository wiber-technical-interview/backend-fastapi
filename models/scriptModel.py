
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

# Script Model base
class Script(BaseModel):
    id:Optional[str] = None
    identifier:Optional[str] = None
    creationDate: Optional[datetime] = datetime.now()
    updateDate: Optional[datetime] = datetime.now()
    name:str
    script:Text
