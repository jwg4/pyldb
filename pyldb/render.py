from jinja2 import Environment, PackageLoader, select_autoescape

from .retrieve import get_board

env = Environment(
    loader=PackageLoader('pyldb', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_board(board, style='board'):
    template_name = '%s.html.js' % (style,)
    template = env.get_template(template_name)
    return template.render(board=board)