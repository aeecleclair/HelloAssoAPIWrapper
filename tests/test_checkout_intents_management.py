from datetime import UTC, datetime

from helloasso_api_wrapper.models.carts import CheckoutPayer, InitCheckoutBody
from tests.commons import hello_asso, organization_slug

checkout_intent_id: int


def test_init_a_checkout() -> None:
    init_checkout_body = InitCheckoutBody(
        totalAmount=100,
        initialAmount=100,
        itemName="test",
        backUrl="https://google.fr",
        errorUrl="https://google.fr",
        returnUrl="https://google.fr",
        containsDonation=False,
        payer=CheckoutPayer(dateOfBirth=datetime(1990, 1, 1, tzinfo=UTC)),
    )

    response = hello_asso.checkout_intents_management.init_a_checkout(
        organization_slug,
        init_checkout_body,
    )

    global checkout_intent_id
    checkout_intent_id = response.id


def test_retrieve_a_checkout_intent() -> None:
    hello_asso.checkout_intents_management.retrieve_a_checkout_intent(
        organization_slug,
        checkout_intent_id,
    )
