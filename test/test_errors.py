from unittest import TestCase

from pyldb import get_board


class TestRetrieveAndRender(TestCase):
    def test_bad_token(self):
        token = "blah-blah-blah-ASDF-QWERTY"
        self.assertRaises(Exception, lambda: get_board("CLJ", token))
