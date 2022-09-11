from __future__ import annotations

import sys
from typing import Any, Dict, Generator, NamedTuple, Optional

from cloudscraper import CloudScraper

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


class Intro(NamedTuple):
    number: int
    name: str
    description: str


class Balaboba:
    """Wrapper for Yandex Balaboba."""

    __slots__ = ("session",)

    def __init__(self, session: Optional[CloudScraper] = None) -> None:
        """Wrapper for Yandex Balaboba.

        Args:
            session: Instance of cloudscraper.CloudScraper. By default,
                a new instance is created for each request.
        """
        self.session = session

    def intros(
        self, language: Literal["en", "ru"] = "ru"
    ) -> Generator[Intro, None, None]:
        """Get text types."""
        endpoint = "intros" if language == "ru" else "intros_eng"
        response = self._get_response(method="GET", endpoint=endpoint)
        return (Intro(*intro) for intro in response["intros"])

    def balaboba(self, query: str, *, intro: int) -> str:
        """Get an answer from Balaboba.

        Args:
            query: Text for Balaboba.
            intro: Text type number. You can get the list of types using
                the intros method.
        """
        response = self._get_response(
            method="POST",
            endpoint="text3",
            json={"query": query, "intro": intro, "filter": 1},
        )
        return f"{response['query']}{response['text']}"

    def _get_response(
        self,
        *,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if isinstance(self.session, CloudScraper):
            return self._fetch(
                method=method,
                endpoint=endpoint,
                json=json,
                session=self.session,
            )
        with CloudScraper.create_scraper() as session:
            return self._fetch(
                method=method, endpoint=endpoint, json=json, session=session
            )

    def _fetch(
        self,
        *,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]],
        session: CloudScraper,
    ) -> Any:
        with session.request(
            method, f"https://yandex.ru/lab/api/yalm/{endpoint}", json=json
        ) as response:
            response.raise_for_status()
            return response.json()
