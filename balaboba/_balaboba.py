from __future__ import annotations

import urllib.parse
from typing import Dict, List, Literal, Optional, Union

from requests import Session

from ._http import HTTPSession
from ._text_type import TextType


class Balaboba:
    """Wrapper for Yandex Balaboba.

    Examples:
        ```python
        from balaboba import Balaboba

        bb = Balaboba()
        text_types = bb.get_text_types(language="en")
        print(text_types)
        response = bb.balaboba("Hello", text_type=text_types[0])
        print(response)
        ```
    """

    __slots__ = ("_session",)

    def __init__(self, session: Optional[Session] = None) -> None:
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
        response = self._session.get_response(
            method="GET",
            endpoint=endpoint,
            headers=self._get_text_types_headers(),
        )
        return [TextType(*intro) for intro in response["intros"]]

    def balaboba(self, query: str, text_type: Union[TextType, int]) -> str:
        intro = (
            text_type.number if isinstance(text_type, TextType) else text_type
        )
        response = self._session.get_response(
            method="POST",
            endpoint="text3",
            json={"query": query, "intro": intro, "filter": 1},
            headers=self._get_balaboba_headers(query, intro),
        )
        return "{}{}".format(response["query"], response["text"])

    def _get_text_types_headers(self) -> Dict[str, str]:
        return {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; rv:109.0)"
                " Gecko/20100101 Firefox/115.0"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://yandex.ru/lab/yalm",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
        }

    def _get_balaboba_headers(
        self, query: str, text_type: int
    ) -> Dict[str, str]:
        return {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; rv:109.0)"
                " Gecko/20100101 Firefox/115.0"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": f"https://yandex.ru/lab/yalm?style={text_type}",
            "X-Requested-With": "XMLHttpRequest",
            "X-Retpath-Y": (
                "https://yandex.ru/lab/yalm?style={}&input={}&skipCurtain=1"
                .format(text_type, urllib.parse.quote_plus(query))
            ),
            "Origin": "https://yandex.ru",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
        }
