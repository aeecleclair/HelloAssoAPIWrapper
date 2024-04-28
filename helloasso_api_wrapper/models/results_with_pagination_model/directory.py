# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T15:09:13+00:00

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from helloasso_api_wrapper.models import directory
    from helloasso_api_wrapper.models.common import PaginationModel


class SynchronizableFormModel(BaseModel):
    data: list[directory.SynchronizableFormModel] | None = None
    pagination: PaginationModel | None = None


class SynchronizableOrganizationModel(BaseModel):
    data: list[directory.SynchronizableOrganizationModel] | None = None
    pagination: PaginationModel | None = None


class PartnerOrganizationModel(BaseModel):
    data: list[directory.PartnerOrganizationModel] | None = None
    pagination: PaginationModel | None = None
