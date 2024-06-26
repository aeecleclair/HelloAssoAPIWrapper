# generated by datamodel-codegen:
#   filename:  HelloAssoV5OpenAPI.json
#   timestamp: 2024-04-28T15:09:13+00:00

from __future__ import annotations

from enum import Enum


class FormType(str, Enum):
    CrowdFunding = "CrowdFunding"
    Membership = "Membership"
    Event = "Event"
    Donation = "Donation"
    PaymentForm = "PaymentForm"
    Checkout = "Checkout"
    Shop = "Shop"


class OrganizationType(Enum):
    Association1901Rig = "Association1901Rig"
    Association1901Rup = "Association1901Rup"
    Association1901 = "Association1901"
    FondationRup = "FondationRup"
    FondDotation = "FondDotation"
    FondationSousEgide = "FondationSousEgide"
    FondationScientifique = "FondationScientifique"
    FondationPartenariale = "FondationPartenariale"
    FondationUniversitaire = "FondationUniversitaire"
    FondationHospitaliere = "FondationHospitaliere"
    Association1905 = "Association1905"
    Association1905Rup = "Association1905Rup"
    Entreprise = "Entreprise"
    Cooperative = "Cooperative"
    Etablissement = "Etablissement"
    Association1908 = "Association1908"
    Association1908Rig = "Association1908Rig"
    Association1908Rup = "Association1908Rup"


class PriceCategory(Enum):
    Fixed = "Fixed"
    Pwyw = "Pwyw"
    Free = "Free"


class TierType(Enum):
    Donation = "Donation"
    Payment = "Payment"
    Registration = "Registration"
    Membership = "Membership"
    MonthlyDonation = "MonthlyDonation"
    MonthlyPayment = "MonthlyPayment"
    OfflineDonation = "OfflineDonation"
    Contribution = "Contribution"
    Bonus = "Bonus"
    Product = "Product"


class ItemState(Enum):
    Processed = "Processed"
    Registered = "Registered"
    Unknown = "Unknown"
    Canceled = "Canceled"


class PaymentCashOutState(Enum):
    MoneyIn = "MoneyIn"
    CantTransferReceiverFull = "CantTransferReceiverFull"
    Transfered = "Transfered"
    Refunded = "Refunded"
    Refunding = "Refunding"
    WaitingForCashOutConfirmation = "WaitingForCashOutConfirmation"
    CashedOut = "CashedOut"
    Unknown = "Unknown"
    Contested = "Contested"
    TransferInProgress = "TransferInProgress"


class PaymentMeans(Enum):
    None_ = "None"
    Card = "Card"
    Check = "Check"
    Cash = "Cash"
    BankTransfer = "BankTransfer"
    Other = "Other"


class PaymentState(Enum):
    Pending = "Pending"
    Authorized = "Authorized"
    Refused = "Refused"
    Unknown = "Unknown"
    Registered = "Registered"
    Refunded = "Refunded"
    Refunding = "Refunding"
    Contested = "Contested"


class PaymentType(Enum):
    Offline = "Offline"
    Credit = "Credit"
    Debit = "Debit"


class FieldType(Enum):
    Date = "Date"
    TextInput = "TextInput"
    FreeText = "FreeText"
    ChoiceList = "ChoiceList"
    File = "File"
    YesNo = "YesNo"
    Phone = "Phone"
    Zipcode = "Zipcode"
    Number = "Number"


class OperationState(Enum):
    UNKNOWN = "UNKNOWN"
    INIT = "INIT"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    ERROR = "ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class RecordActionType(Enum):
    Insert = "Insert"
    Delete = "Delete"


class MembershipValidityType(Enum):
    MovingYear = "MovingYear"
    Custom = "Custom"
    Illimited = "Illimited"


class FormState(Enum):
    Public = "Public"
    Private = "Private"
    Draft = "Draft"
    Disabled = "Disabled"


class PaymentFrequencyType(Enum):
    Single = "Single"
    Installment = "Installment"
    Monthly = "Monthly"


class TagType(Enum):
    Explore = "Explore"
    Internal = "Internal"


class GlobalRole(Enum):
    OrganizationAdmin = "OrganizationAdmin"
    FormAdmin = "FormAdmin"


class SortOrder(Enum):
    Asc = "Asc"
    Desc = "Desc"


class SortField(Enum):
    Date = "Date"
    UpdateDate = "UpdateDate"
    CreationDate = "CreationDate"
