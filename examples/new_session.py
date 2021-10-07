#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from balaboba import balaboba

# Используется стандартный вариант стилизации.
# Для запроса создаётся новый экземпляр requests.Session.
response = balaboba("Привет")
print(response)
