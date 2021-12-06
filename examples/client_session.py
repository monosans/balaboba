#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Используется существующий экземпляр requests.Session."""
from balaboba import balaboba
from requests import Session

with Session() as session:
    response = balaboba("Привет", session=session)
print(response)
