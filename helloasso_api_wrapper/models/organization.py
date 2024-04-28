# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T15:09:13+00:00

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from helloasso_api_wrapper.models import enums

if TYPE_CHECKING:
    from datetime import datetime

    from helloasso_api_wrapper.models import shared


class OrganizationBasicModel(BaseModel):
    url: str | None = None
    organizationSlug: str | None = None


class OrganizationModel(BaseModel):
    isAuthenticated: bool | None = None
    banner: str | None = None
    fiscalReceiptEligibility: bool | None = None
    fiscalReceiptIssuanceEnabled: bool | None = None
    type: enums.OrganizationType | None = None
    category: str | None = None
    address: str | None = None
    geolocation: shared.GeoLocation | None = None
    rnaNumber: str | None = None
    logo: str | None = None
    name: str | None = None
    role: enums.GlobalRole | None = None
    city: str | None = None
    zipCode: str | None = None
    description: str | None = None
    updateDate: datetime | None = None
    url: str | None = None
    organizationSlug: str | None = None


class OrganizationLightModel(BaseModel):
    logo: str | None = None
    name: str | None = None
    role: enums.GlobalRole | None = None
    city: str | None = None
    zipCode: str | None = None
    description: str | None = None
    updateDate: datetime | None = None
    url: str | None = None
    organizationSlug: str | None = None