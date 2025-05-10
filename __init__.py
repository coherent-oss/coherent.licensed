import requests


def resolve(expression):
    """
    Resolve an SPDX license expression into a license text.

    >>> resolve('MIT')
    'MIT License...'
    """
    url = f"https://raw.githubusercontent.com/spdx/license-list-data/main/text/{expression}.txt"
    return requests.get(url).text
