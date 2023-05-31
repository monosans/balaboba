from __future__ import annotations

from typing import Any, Mapping, Optional

from requests import Response, Session


class HTTPSession:
    __slots__ = ("session",)

    def __init__(self, session: Optional[Session]) -> None:
        self.session = session

    def get_response(
        self,
        *,
        method: str,
        endpoint: str,
        json: Any = None,
        headers: Mapping[str, str],
    ) -> Any:
        if isinstance(self.session, Session):
            response = self._fetch(
                method=method,
                endpoint=endpoint,
                json=json,
                headers=headers,
                session=self.session,
            )
        else:
            with Session() as session:
                response = self._fetch(
                    method=method,
                    endpoint=endpoint,
                    json=json,
                    headers=headers,
                    session=session,
                )
        response.raise_for_status()
        return response.json()

    def _fetch(
        self,
        *,
        method: str,
        endpoint: str,
        json: Any,
        headers: Mapping[str, str],
        session: Session,
    ) -> Response:
        with session.request(
            method,
            f"https://yandex.ru/lab/api/yalm/{endpoint}",
            json=json,
            headers=headers,
        ) as response:
            return response
