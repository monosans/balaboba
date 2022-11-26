from __future__ import annotations

import sys
from random import choice
from typing import Optional, Type

import pytest
from requests import Session

from balaboba import Balaboba

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


@pytest.mark.parametrize("session_type", (None, Session))
@pytest.mark.parametrize("language", ("en", "ru"))
@pytest.mark.parametrize("query", ("Привет", "Hello"))
def test_balaboba(
    session_type: Optional[Type[Session]],
    language: Literal["en", "ru"],
    query: str,
) -> None:
    session = Session() if session_type else None
    try:
        b = Balaboba(session=session)
        text_types = b.get_text_types(language)
        response = b.balaboba(query, text_type=choice(text_types).number)
    finally:
        if isinstance(session, Session):
            session.close()
    assert len(response) >= len(query)
    assert query.lower() in response.lower()
