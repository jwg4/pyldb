import os

from unittest import TestCase

import requests

from pyldb import get_board, render_board


class TestRender(TestCase):
    def test_do_a_render(self):
        """
            This tst depends on two external services:
            the LDBWS service itself, and the W3C HTML
            validator service. So there should be at least
            some expectation that it might fail because
            of problems with or problems connecting to
            those services, even if no code has changed.
        """
        token = os.environ["PYLDB_API_TOKEN"]
        data = get_board("VIC", token)
        html = render_board(data)
        self.validate(html)

    def validate(self, html):
        self.assertIsNotNone(html)

        r = requests.post(
            'https://validator.w3.org/nu/',
            data=html,
            params={'out': 'json'},
            headers={'Content-Type': 'text/html; charset=UTF-8'}
        )
        result = r.json()
        messages = result['messages']
        errors = [ m for m in messages if m['type'] == 'error' ]
        self.assertListEqual([], errors)
