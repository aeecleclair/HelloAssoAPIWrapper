# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T15:09:13+00:00

from __future__ import annotations

from pydantic import BaseModel


class OrganismCategoryModel(BaseModel):
    id: int | None = None
    label: str | None = None
    shortLabel: str | None = None


class CompanyLegalStatusModel(BaseModel):
    id: int | None = None
    label: str | None = None
