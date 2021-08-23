from flask import (
    Blueprint,
    render_template
)
from app.db import get_db

#from flask.templating import render_template

bp = Blueprint('mail', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute("SELECT * FROM email")
    mails = c.fetchall()

    return render_template('mails/index.html', mails=mails)



@bp.route('/create', methods=['GET','POST'])
def create():
    return render_template('mails/create.html')
