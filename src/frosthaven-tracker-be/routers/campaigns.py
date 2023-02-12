from enum import Enum

from fastapi import APIRouter
from pony import orm
from pydantic import BaseModel


class Game(Enum):
    FROSTHAVEN = "Frosthaven"
    GLOOMHAVEM = "Gloomhaven"
    JAWS_OF_THE_LION = "Jaws of the Lion"


class CampaignSchema(BaseModel):
    party_name: str
    game: Game


router = APIRouter()


@orm.db_session
@router.get("/campaigns/{campaign_id}", tags=["campaigns"])
async def get_campaign(campaign_id: int):
    pass


@orm.db_session
@router.post("/campaigns/", tags=["campaigns"])
async def create_campaign(campaign: CampaignSchema):
    return campaign
