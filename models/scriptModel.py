
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from typing import List,Optional



class DescriptionScript(BaseModel):
    name: str
    script: Text
class UpdateScript(BaseModel):
    name:str
    description:Text


class Script(BaseModel):
    creationDate: Optional[datetime] = datetime.now()
    name: str
    script: List[DescriptionScript]