from __future__ import annotations

from typing import Literal

import pytest
from requests import Session

from balaboba import Balaboba


@pytest.mark.parametrize(
    ("language", "query"), [("en", "Hello"), ("ru", "Привет")]
)
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
