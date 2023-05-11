from __future__ import annotations

import sys

import pytest
from requests import JSONDecodeError, Session

from balaboba import Balaboba

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from typing_extensions import Literal
else:  # pragma: >=3.8 cover
    from typing import Literal


@pytest.mark.parametrize(("language", "query"), [("en", "Hello"), ("ru", "Привет")])
def test_balaboba(language: Literal["en", "ru"], query: str) -> None:
    b = Balaboba()
    assert b.session is None
    text_types = b.get_text_types(language)
    with Session() as session:
        b.session = session
        assert b.session is session
        try:
            response = b.balaboba(query, text_type=text_types[0])
        except JSONDecodeError:  # pragma: no cover
            pass
        else:  # pragma: no cover
            assert len(response) >= len(query)
            assert query.lower() in response.lower()
