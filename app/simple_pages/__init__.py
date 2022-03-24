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
    result = 0
    if page == 'index':
        result = 1
    elif page == 'git':
        result = 2
    elif page == 'docker':
        result = 3
    elif page == 'flask':
        result = 4
    elif page == 'CICD':
        result = 5
    elif page == 'OOPs':
        result = 6
    elif page == 'SOLID':
        result = 7
    return result
