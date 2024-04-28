from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from datetime import datetime

    from helloasso_api_wrapper.models import shared


class MetaModel(BaseModel):
    createdAt: datetime | None = None
    updatedAt: datetime | None = None


class PaginationModel(BaseModel):
    pageSize: int | None = None
    totalCount: int | None = None
    pageIndex: int | None = None
    totalPages: int | None = None
    continuationToken: str | None = None


class ContactModel(BaseModel):
    email: str | None = None
    phoneNumber: str | None = None


class DocumentModel(BaseModel):
    id: int | None = None
    fileName: str | None = None
    publicUrl: str | None = None


class PlaceModel(BaseModel):
    address: str | None = None
    name: str | None = None
    city: str | None = None
    zipCode: str | None = None
    country: constr(min_length=3, max_length=3) | None = None
    geoLocation: shared.GeoLocation | None = None
