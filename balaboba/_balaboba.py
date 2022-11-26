from __future__ import annotations

import sys
from typing import List, Optional, Union

from requests import Session

from ._http import HTTPSession
from ._text_type import TextType

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


class Balaboba:
    """Wrapper for Yandex Balaboba."""

    __slots__ = ("_session",)

    def __init__(self, session: Optional[Session] = None) -> None:
        """Wrapper for Yandex Balaboba."""
        self._session = HTTPSession(session)

    @property
    def session(self) -> Optional[Session]:
        return self._session.session

    @session.setter
    def session(self, session: Optional[Session]) -> None:
        self._session.session = session

    def get_text_types(
        self, language: Literal["en", "ru"] = "ru"
    ) -> List[TextType]:
        endpoint = "intros" if language == "ru" else "intros_eng"
        response = self._session.get_response(method="GET", endpoint=endpoint)
        return [TextType(*intro) for intro in response["intros"]]

    def balaboba(self, query: str, text_type: Union[TextType, int]) -> str:
        intro = (
            text_type.number if isinstance(text_type, TextType) else text_type
        )
        response = self._session.get_response(
            method="POST",
            endpoint="text3",
            json={"query": query, "intro": intro, "filter": 1},
        )
        return "{}{}".format(response["query"], response["text"])
