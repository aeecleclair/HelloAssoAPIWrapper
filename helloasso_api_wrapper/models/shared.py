# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T19:01:23+00:00

from __future__ import annotations

from pydantic import BaseModel


class GeoLocation(BaseModel):
    latitude: float | None = None
    longitude: float | None = None
