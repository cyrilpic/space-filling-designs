# -*- coding: utf-8 -*-
"""Main module."""
import requests
from lxml import html

base_url = {
    'maximin': 'https://spacefillingdesigns.nl/maximin/{type}.php?n={n}&m={m}'
}


def extract_design_from_url(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    design = []
    for tr in tree.xpath('//table/tr'):
        design.append(list(map(int, tr.xpath('td/text()'))))
    return design


def get_maximin_design(type, n, m):
    url = base_url['maximin'].format(type=type, n=n, m=m)
    return extract_design_from_url(url)
