# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T15:09:13+00:00

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from helloasso_api_wrapper.models import common, enums


class Payer(BaseModel):
    email: str | None = None
    address: str | None = None
    city: str | None = None
    zipCode: str | None = None
    country: str | None = None
    company: str | None = None
    dateOfBirth: datetime | None = None
    firstName: str | None = None
    lastName: str | None = None


class OrderAmountModel(BaseModel):
    total: int | None = None
    vat: int | None = None
    discount: int | None = None


class SharePayment(BaseModel):
    id: int | None = None
    shareAmount: int | None = None


class User(BaseModel):
    firstName: str | None = None
    lastName: str | None = None


class ItemDiscount(BaseModel):
    code: str | None = None
    amount: int | None = None


class ItemCustomField(BaseModel):
    id: int | None = None
    name: str | None = None
    type: enums.FieldType | None = None
    answer: str | None = None


class ItemOption(BaseModel):
    name: str | None = None
    amount: int | None = None
    priceCategory: enums.PriceCategory | None = None
    isRequired: bool | None = None
    customFields: list[ItemCustomField] | None = None
    optionId: int | None = None


class ShareItem(BaseModel):
    id: int | None = None
    shareAmount: int | None = None
    shareItemAmount: int | None = None
    shareOptionsAmount: int | None = None


class RefundOperationLightModel(BaseModel):
    id: int | None = None
    amount: int | None = None
    amountTip: int | None = None
    status: enums.OperationState | None = None
    meta: common.MetaModel | None = None


class OrderLight(BaseModel):
    id: int | None = None
    date: datetime | None = None
    formSlug: str | None = None
    formType: enums.FormType | None = None
    organizationName: str | None = None
    organizationSlug: str | None = None
    organizationType: enums.OrganizationType | None = None
    organizationIsUnderColucheLaw: bool | None = None
    checkoutIntentId: int | None = None
    meta: common.MetaModel | None = None


class ItemPayment(BaseModel):
    cashOutState: enums.PaymentCashOutState | None = None
    shareAmount: int | None = None
    id: int | None = None
    amount: int | None = None
    amountTip: int | None = None
    date: datetime | None = None
    paymentMeans: enums.PaymentMeans | None = None
    installmentNumber: int | None = None
    state: enums.PaymentState | None = None
    type: enums.PaymentType | None = None
    meta: common.MetaModel | None = None
    paymentOffLineMean: enums.PaymentMeans | None = None
    refundOperations: list[RefundOperationLightModel] | None = None


class Item(BaseModel):
    order: OrderLight | None = None
    payer: Payer | None = None
    payments: list[ItemPayment] | None = None
    name: str | None = None
    user: User | None = None
    priceCategory: enums.PriceCategory | None = None
    minAmount: int | None = None
    discount: ItemDiscount | None = None
    customFields: list[ItemCustomField] | None = None
    options: list[ItemOption] | None = None
    ticketUrl: str | None = None
    qrCode: str | None = None
    membershipCardUrl: str | None = None
    dayOfLevy: int | None = None
    tierDescription: str | None = None
    tierId: int | None = None
    comment: str | None = None
    id: int | None = None
    amount: int | None = None
    type: enums.TierType | None = None
    initialAmount: int | None = None
    state: enums.ItemState | None = None


class PaymentItem(BaseModel):
    shareAmount: int | None = None
    shareItemAmount: int | None = None
    shareOptionsAmount: int | None = None
    id: int | None = None
    amount: int | None = None
    type: enums.TierType | None = None
    initialAmount: int | None = None
    state: enums.ItemState | None = None
    name: str | None = None


class Payment(BaseModel):
    order: OrderLight | None = None
    payer: Payer | None = None
    items: list[PaymentItem] | None = None
    cashOutDate: datetime | None = None
    cashOutState: enums.PaymentCashOutState | None = None
    paymentReceiptUrl: str | None = None
    fiscalReceiptUrl: str | None = None
    id: int | None = None
    amount: int | None = None
    amountTip: int | None = None
    date: datetime | None = None
    paymentMeans: enums.PaymentMeans | None = None
    installmentNumber: int | None = None
    state: enums.PaymentState | None = None
    type: enums.PaymentType | None = None
    meta: common.MetaModel | None = None
    paymentOffLineMean: enums.PaymentMeans | None = None
    refundOperations: list[RefundOperationLightModel] | None = None


class OrderItem(BaseModel):
    payments: list[SharePayment] | None = None
    name: str | None = None
    user: User | None = None
    priceCategory: enums.PriceCategory | None = None
    minAmount: int | None = None
    discount: ItemDiscount | None = None
    customFields: list[ItemCustomField] | None = None
    options: list[ItemOption] | None = None
    ticketUrl: str | None = None
    qrCode: str | None = None
    membershipCardUrl: str | None = None
    dayOfLevy: int | None = None
    tierDescription: str | None = None
    tierId: int | None = None
    comment: str | None = None
    id: int | None = None
    amount: int | None = None
    type: enums.TierType | None = None
    initialAmount: int | None = None
    state: enums.ItemState | None = None


class OrderPayment(BaseModel):
    items: list[ShareItem] | None = None
    cashOutDate: datetime | None = None
    cashOutState: enums.PaymentCashOutState | None = None
    paymentReceiptUrl: str | None = None
    fiscalReceiptUrl: str | None = None
    id: int | None = None
    amount: int | None = None
    amountTip: int | None = None
    date: datetime | None = None
    paymentMeans: enums.PaymentMeans | None = None
    installmentNumber: int | None = None
    state: enums.PaymentState | None = None
    type: enums.PaymentType | None = None
    meta: common.MetaModel | None = None
    paymentOffLineMean: enums.PaymentMeans | None = None
    refundOperations: list[RefundOperationLightModel] | None = None


class ItemDetail(BaseModel):
    order: OrderLight | None = None
    payer: Payer | None = None
    payments: list[ItemPayment] | None = None
    name: str | None = None
    user: User | None = None
    priceCategory: enums.PriceCategory | None = None
    minAmount: int | None = None
    discount: ItemDiscount | None = None
    customFields: list[ItemCustomField] | None = None
    options: list[ItemOption] | None = None
    ticketUrl: str | None = None
    qrCode: str | None = None
    membershipCardUrl: str | None = None
    dayOfLevy: int | None = None
    tierDescription: str | None = None
    tierId: int | None = None
    comment: str | None = None
    id: int | None = None
    amount: int | None = None
    type: enums.TierType | None = None
    initialAmount: int | None = None
    state: enums.ItemState | None = None


class Order(BaseModel):
    payer: Payer | None = None
    items: list[OrderItem] | None = None
    payments: list[OrderPayment] | None = None
    amount: OrderAmountModel | None = None
    id: int | None = None
    date: datetime | None = None
    formSlug: str | None = None
    formType: enums.FormType | None = None
    organizationName: str | None = None
    organizationSlug: str | None = None
    organizationType: enums.OrganizationType | None = None
    organizationIsUnderColucheLaw: bool | None = None
    checkoutIntentId: int | None = None
    meta: common.MetaModel | None = None


class PaymentDetail(BaseModel):
    order: OrderLight | None = None
    payer: Payer | None = None
    items: list[PaymentItem] | None = None
    cashOutDate: datetime | None = None
    cashOutState: enums.PaymentCashOutState | None = None
    paymentReceiptUrl: str | None = None
    fiscalReceiptUrl: str | None = None
    id: int | None = None
    amount: int | None = None
    amountTip: int | None = None
    date: datetime | None = None
    paymentMeans: enums.PaymentMeans | None = None
    installmentNumber: int | None = None
    state: enums.PaymentState | None = None
    type: enums.PaymentType | None = None
    meta: common.MetaModel | None = None
    paymentOffLineMean: enums.PaymentMeans | None = None
    refundOperations: list[RefundOperationLightModel] | None = None


class OrderDetail(BaseModel):
    payer: Payer | None = None
    items: list[OrderItem] | None = None
    payments: list[OrderPayment] | None = None
    amount: OrderAmountModel | None = None
    id: int | None = None
    date: datetime | None = None
    formSlug: str | None = None
    formType: enums.FormType | None = None
    organizationName: str | None = None
    organizationSlug: str | None = None
    organizationType: enums.OrganizationType | None = None
    organizationIsUnderColucheLaw: bool | None = None
    checkoutIntentId: int | None = None
    meta: common.MetaModel | None = None
