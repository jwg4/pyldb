from unittest import TestCase

import requests

from pyldb import render_board


class TestHTMLOutput(TestCase):
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


class TestRender(TestHTMLOutput):
    class StationBoardStub(object):
        crs = "CLJ"
        locationName = "Clapham Junction"
        generatedAt = "2020-04-18T02:33:50.6760206+01:00"

    def test_render_board_without_trains(self):
        data = TestRender.StationBoardStub()
        html = render_board(data)
        self.validate(html)
