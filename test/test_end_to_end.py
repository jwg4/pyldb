import os

from pyldb import get_board, render_board

from test.test_rendering import TestHTMLOutput


class TestRetrieveAndRender(TestHTMLOutput):
    def test_do_a_render(self):
        """
            This test depends on two external services:
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
