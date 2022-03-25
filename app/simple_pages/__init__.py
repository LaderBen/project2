from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_page', __name__,
                         template_folder='templates', static_folder='static')


@simple_pages.route('/', defaults={'page': 'index'})
@simple_pages.route('/<page>')
def show(page):
    try:
        i = highlight(page)
        return render_template('%s.html' % page, name="Benchuan's", page_highlight=i)
    except TemplateNotFound:
        abort(404)


def highlight(page):
    if page == 'index':
        return 1
    elif page == 'git':
        return 2
    elif page == 'docker':
        return 3
    elif page == 'flask':
        return 4
    elif page == 'CICD':
        return 5
    elif page == 'OOPs':
        return 6
    elif page == 'SOLID':
        return 7
    elif page == 'AAA':
        return 8
    elif page == 'pylint':
        return 9
