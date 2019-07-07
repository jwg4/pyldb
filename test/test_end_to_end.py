import os

from unittest import TestCase

from pyldb import get_board, render_board


class TestRender(TestCase):
    def test_do_a_render(self):
        token = os.environ["PYLDB_API_TOKEN"]
        data = get_board("VIC", token)
        html = render_board(data)
        self.assertIsNotNone(html)
