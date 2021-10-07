#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from balaboba import balaboba
from requests import Session

with Session() as session:
    # Используется 11-ый вариант стилизации "Народные мудрости".
    # Для запроса используется существующий экземпляр requests.Session.
    response = balaboba("Привет", intro=11, session=session)
print(response)
