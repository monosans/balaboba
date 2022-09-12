from __future__ import annotations

import sys
from random import choice
from typing import Optional, Type

import pytest
from cloudscraper import CloudScraper

from balaboba import Balaboba

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


@pytest.mark.parametrize("session_type", (None, CloudScraper))
@pytest.mark.parametrize("language", ("en", "ru"))
@pytest.mark.parametrize("query", ("Привет", "Hello"))
def test_balaboba(
    session_type: Optional[Type[CloudScraper]],
    language: Literal["en", "ru"],
    query: str,
) -> None:
    try:
        session = CloudScraper.create_scraper() if session_type else None
        b = Balaboba(session=session)
        intros = tuple(b.intros(language))
        response = b.balaboba(query, intro=choice(intros).number)
    finally:
        if isinstance(session, CloudScraper):
            session.close()
    assert len(response) >= len(query)
    assert query.lower() in response.lower()
