# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T15:09:13+00:00

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, constr

if TYPE_CHECKING:
    from datetime import datetime

    from helloasso_api_wrapper.models import common, enums


class FormBasicModel(BaseModel):
    formSlug: str | None = None
    formType: enums.FormType | None = None
    url: str | None = None
    organizationSlug: str | None = None


class TierLightModel(BaseModel):
    label: str | None = None
    price: int | None = None


class FormQuickCreateModel(BaseModel):
    formSlug: str | None = None
    organizationSlug: str | None = None
    publicUrl: str | None = None


class TermModel(BaseModel):
    date: datetime | None = None
    amount: int | None = None


class FormLightModel(BaseModel):
    banner: common.DocumentModel | None = None
    currency: str | None = None
    description: str | None = None
    startDate: datetime | None = None
    endDate: datetime | None = None
    logo: common.DocumentModel | None = None
    meta: common.MetaModel | None = None
    state: enums.FormState | None = None
    title: str | None = None
    privateTitle: str | None = None
    widgetButtonUrl: str | None = None
    widgetFullUrl: str | None = None
    widgetVignetteHorizontalUrl: str | None = None
    widgetVignetteVerticalUrl: str | None = None
    widgetCounterUrl: str | None = None
    formSlug: str | None = None
    formType: enums.FormType | None = None
    url: str | None = None
    organizationSlug: str | None = None


class TierPublicModel(BaseModel):
    id: int | None = None
    label: str | None = None
    description: str | None = None
    tierType: enums.TierType | None = None
    price: int | None = None
    vatRate: float | None = None
    minAmount: int | None = None
    paymentFrequency: enums.PaymentFrequencyType | None = None
    maxPerUser: int | None = None
    meta: common.MetaModel | None = None
    saleStartDate: datetime | None = None
    saleEndDate: datetime | None = None
    isEligibleTaxReceipt: bool | None = None
    terms: list[TermModel] | None = None
    picture: common.DocumentModel | None = None


class FormQuickCreateRequest(BaseModel):
    tierList: list[TierLightModel] | None = None
    banner: str | None = None
    description: str | None = None
    endDate: datetime | None = None
    logo: str | None = None
    privateTitle: str | None = None
    startDate: datetime | None = None
    title: str
    activityTypeId: int | None = None
    place: common.PlaceModel | None = None
    saleEndDate: datetime | None = None
    saleStartDate: datetime | None = None
    validityType: enums.MembershipValidityType | None = None
    acceptOpenDonation: bool | None = None
    allowComment: bool | None = None
    amountVisible: bool | None = None
    color: str | None = None
    widgetButtonText: str | None = None
    contact: common.ContactModel | None = None
    displayContributorName: bool | None = None
    displayParticipantsCount: bool | None = None
    displayRemainingEntries: bool | None = None
    financialGoal: int | None = None
    generateMembershipCards: bool | None = None
    generateTickets: bool | None = None
    invertDescriptions: bool | None = None
    labelConditionsAndTermsFile: str | None = None
    longDescription: str | None = None
    openDonationPresetAmounts: list[int] | None = None
    personalizedMessage: str | None = None
    projectBeneficiaries: str | None = None
    projectExpensesDetails: str | None = None
    projectOwners: str | None = None
    projectTargetCountry: constr(min_length=3, max_length=3) | None = None
    maxEntries: int | None = None


class FormPublicModel(BaseModel):
    organizationLogo: str | None = None
    organizationName: str | None = None
    tiers: list[TierPublicModel] | None = None
    activityType: str | None = None
    activityTypeId: int | None = None
    place: common.PlaceModel | None = None
    saleEndDate: datetime | None = None
    saleStartDate: datetime | None = None
    validityType: enums.MembershipValidityType | None = None
    banner: common.DocumentModel | None = None
    currency: str | None = None
    description: str | None = None
    startDate: datetime | None = None
    endDate: datetime | None = None
    logo: common.DocumentModel | None = None
    meta: common.MetaModel | None = None
    state: enums.FormState | None = None
    title: str | None = None
    privateTitle: str | None = None
    widgetButtonUrl: str | None = None
    widgetFullUrl: str | None = None
    widgetVignetteHorizontalUrl: str | None = None
    widgetVignetteVerticalUrl: str | None = None
    widgetCounterUrl: str | None = None
    formSlug: str | None = None
    formType: enums.FormType | None = None
    url: str | None = None
    organizationSlug: str | None = None