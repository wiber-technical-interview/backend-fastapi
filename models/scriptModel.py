
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from typing import List,Optional



class DescriptionScript(BaseModel):
    name: str
    script: Text

class Script(BaseModel):
    identifier: Optional[str] = None
    creationDate: Optional[datetime] = datetime.now()
    name: str
    script: List[DescriptionScript]