from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_page', __name__,
                        template_folder='templates',static_folder='static')


@simple_pages.route('/', defaults={'page': 'index'})
@simple_pages.route('/<page>')
def show(page):
    try:
        i,g,d,f,c = highlight(page)
        return render_template('%s.html' % page, name="Benchuan's", index=i,git=g,docker=d,flask=f,CICD=c)
    except TemplateNotFound:
        abort(404)

def highlight(page):
    index = False
    git = False
    docker = False
    flask = False
    CICD = False
    if page == 'index':
        index = True
    elif page == 'git':
        git= True
    elif page == 'docker':
        docker = True
    elif page == 'flask':
        flask = True
    elif page == 'CICD':
        CICD = True
    return  index,git,docker,flask,CICD