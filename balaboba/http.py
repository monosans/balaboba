from __future__ import annotations

from typing import Any, Dict, Optional

from requests import Session


class HTTPSession:
    __slots__ = ("session",)

    def __init__(self, session: Optional[Session]) -> None:
        self.session = session

    def get_response(
        self,
        *,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if isinstance(self.session, Session):
            return self._fetch(
                method=method,
                endpoint=endpoint,
                json=json,
                session=self.session,
            )
        with Session() as session:
            return self._fetch(
                method=method, endpoint=endpoint, json=json, session=session
            )

    def _fetch(
        self,
        *,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]],
        session: Session,
    ) -> Any:
        with session.request(
            method, f"https://yandex.ru/lab/api/yalm/{endpoint}", json=json
        ) as response:
            response.raise_for_status()
            return response.json()
