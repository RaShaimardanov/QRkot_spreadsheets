from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field


MIN_LENGTH_FIELD = 1
MAX_LENGTH_FIELD = 100
GT_NULL_FIELD = 0


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=MIN_LENGTH_FIELD, max_length=MAX_LENGTH_FIELD)
    description: Optional[str] = Field(None, min_length=MIN_LENGTH_FIELD)
    full_amount: Optional[int] = Field(None, gt=GT_NULL_FIELD)

    class Config:
        orm_mode = True
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectUpdate):
    name: str = Field(..., min_length=MIN_LENGTH_FIELD, max_length=MAX_LENGTH_FIELD)
    description: str = Field(..., min_length=MIN_LENGTH_FIELD)
    full_amount: int = Field(..., gt=GT_NULL_FIELD)


class CharityProjectDB(CharityProjectUpdate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime = Field(None)
