from jinja2 import Environment, FileSystemLoader, select_autoescape

from .retrieve import get_board

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_board(board, style='board'):
    template_name = '%s.html.j2' % (style,)
    template = env.get_template(template_name)
    return template.render(board=board)