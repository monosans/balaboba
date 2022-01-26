#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Используется существующий экземпляр cloudscraper.CloudScraper"""
from balaboba import balaboba
from cloudscraper import create_scraper

with create_scraper() as session:
    response = balaboba("Привет", session=session)
print(response)
