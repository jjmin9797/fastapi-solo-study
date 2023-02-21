from pydantic import BaseModel


class RobotsRequestDto(BaseModel):
    url: str
