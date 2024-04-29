from enum import Enum
from typing import Literal

from pydantic import BaseModel

from helloasso_api_wrapper.models.forms import FormPublicModel
from helloasso_api_wrapper.models.statistics import OrderDetail, PaymentDetail


class ApiNotificationType(Enum):
    Payment = "Payment"
    Order = "Order"
    Form = "Form"
    Organization = "Organization"


class PostApiUrlNotificationBody(BaseModel):
    url: str
    notificationType: ApiNotificationType | None = None


class ApiUrlNotificationModel(BaseModel):
    url: str | None = None
    apiNotificationType: ApiNotificationType | None = None


class OrganizationNotificationResultData(BaseModel):
    old_slug_organization: str
    new_slug_organization: str


class NotificationResultContent(BaseModel):
    """
    When a new content is available, HelloAsso will call the notification URL callback with the corresponding data in the body.
    """

    eventType: ApiNotificationType
    data: (
        OrganizationNotificationResultData
        | OrderDetail
        | PaymentDetail
        | FormPublicModel
    )


class OrganizationNotificationResultContent(BaseModel):
    eventType: Literal[ApiNotificationType.Organization]
    data: OrganizationNotificationResultData


class OrderNotificationResultContent(BaseModel):
    eventType: Literal[ApiNotificationType.Order]
    data: OrderDetail


class PayementNotificationResultContent(BaseModel):
    eventType: Literal[ApiNotificationType.Payment]
    data: PaymentDetail


class FormNotificationResultContent(BaseModel):
    eventType: Literal[ApiNotificationType.Form]
    data: FormPublicModel
