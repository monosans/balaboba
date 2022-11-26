from __future__ import annotations

import sys
from typing import Any, Dict, List, NamedTuple, Optional

from requests import Session

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


class TextType(NamedTuple):
    number: int
    name: str
    description: str


class Balaboba:
    """Wrapper for Yandex Balaboba."""

    __slots__ = ("session",)

    def __init__(self, session: Optional[Session] = None) -> None:
        """Wrapper for Yandex Balaboba.

        Args:
            session: Instance of requests.Session. By default,
                a new instance is created for each request.
        """
        self.session = session

    def get_text_types(
        self, language: Literal["en", "ru"] = "ru"
    ) -> List[TextType]:
        endpoint = "intros" if language == "ru" else "intros_eng"
        response = self._get_response(method="GET", endpoint=endpoint)
        return [TextType(*intro) for intro in response["intros"]]

    def balaboba(self, query: str, *, text_type: int) -> str:
        """Get an answer from Balaboba.

        Args:
            query: Text for Balaboba.
            text_type: Text type number. You can get the list of types using
                the get_text_types method.
        """
        response = self._get_response(
            method="POST",
            endpoint="text3",
            json={"query": query, "intro": text_type, "filter": 1},
        )
        return "{}{}".format(response["query"], response["text"])

    def _get_response(
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
