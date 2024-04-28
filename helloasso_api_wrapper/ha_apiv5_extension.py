from collections.abc import Callable
from typing import Literal, TypeVar

from helloasso_api import HaApiV5
from pydantic import BaseModel


class HaApiV5Extension(HaApiV5):
    """
    The class inherit from HaApiV5 and add some methods to serialize the response of the API.
    """

    def __init__(
        self,
        api_base: str,
        client_id: str,
        client_secret: str,
        timeout: int | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        oauth2_token_getter: (
            Callable[
                [Literal["access_token", "refresh_token"], str],
                str,
            ]
            | None
        ) = None,
        oauth2_token_setter: (
            Callable[
                [Literal["access_token", "refresh_token"], str, str],
                None,
            ]
            | None
        ) = None,
    ):
        super().__init__(
            api_base=api_base,
            client_id=client_id,
            client_secret=client_secret,
            timeout=timeout,
            access_token=access_token,
            refresh_token=refresh_token,
            oauth2_token_getter=oauth2_token_getter,
            oauth2_token_setter=oauth2_token_setter,
        )  # type: ignore

    PydanticModel = TypeVar("PydanticModel", bound=BaseModel)

    def callAndSerialize(
        self,
        sub_path: str,
        model: type[PydanticModel],
        params: dict | None = None,
        method: str | None = "GET",
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
        include_auth: bool = True,
    ) -> PydanticModel:
        sub_path = "/v5" + sub_path
        response = self.call(
            sub_path,
            params=params,  # type: ignore
            method=method,  # type: ignore
            data=data,  # type: ignore
            json=json,  # type: ignore
            headers=headers,  # type: ignore
            include_auth=include_auth,
        ).json()

        return model.model_validate(
            response,
        )

    def callAndSerializeList(
        self,
        sub_path: str,
        model: type[PydanticModel],
        params: dict | None = None,
        method: str | None = "GET",
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
        include_auth: bool = True,
    ) -> list[PydanticModel]:
        sub_path = "/v5" + sub_path
        response = self.call(
            sub_path,
            params=params,  # type: ignore
            method=method,  # type: ignore
            data=data,  # type: ignore
            json=json,  # type: ignore
            headers=headers,  # type: ignore
            include_auth=include_auth,
        ).json()

        return [
            model.model_validate(
                obj,
            )
            for obj in response
        ]
