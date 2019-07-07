import os

from unittest import TestCase

from pyldb import get_board, render


class TestRender(TestCase):
    def test_do_a_render(self):
        token = os.environ("PYLDB_API_TOKEN")
        board = get_board("VIC", token)
        html = render(board)
        self.assertIsNotNone(html)
