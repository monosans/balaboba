from __future__ import annotations

import sys
from random import choice

import pytest
from requests import Session

from balaboba import Balaboba

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


@pytest.mark.parametrize("language,query", (("en", "Hello"), ("ru", "Привет")))
def test_balaboba(language: Literal["en", "ru"], query: str) -> None:
    b = Balaboba()
    assert b.session is None
    text_types = b.get_text_types(language)
    with Session() as session:
        b.session = session
        assert b.session is session
        response = b.balaboba(query, text_type=text_types[0])
    assert len(response) >= len(query)
    assert query.lower() in response.lower()
