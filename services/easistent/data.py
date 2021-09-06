from typing import Optional

from pydantic import BaseModel


class School(BaseModel):
	name: str
	id: Optional[int]
	classes: dict
