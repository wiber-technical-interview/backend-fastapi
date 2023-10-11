
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

# Script Model 
class PostScript(BaseModel):
    id:Optional[str] = None
    identifier:Optional[str] = None
    creationDate: Optional[datetime] = datetime.now()
    updateDate: Optional[datetime] = datetime.now()
    name:str
    script:Text
