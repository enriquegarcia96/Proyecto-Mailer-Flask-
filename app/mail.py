from flask import (
    Blueprint,
    render_template,
    request, flash, 
    url_for, redirect
)
from flask.globals import current_app


from app.db import get_db

bp = Blueprint('mail', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute("SELECT * FROM email")
    mails = c.fetchall()

    return render_template('mails/index.html', mails=mails)

@bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []
        
        #print(email, subject, content)

        if not email:
            errors.append('Email es obligatorio')
        if not subject:
            errors.append('Asunto es obligatorio')
        if not content:
            errors.append('Contenido es obligatorio')

        if len(errors) == 0:
            db, c = get_db()
            c.execute("INSERT INTO email (email, subject, content) VALUES (%s, %s, %s)", (email, subject, content))
            db.commit()
            return redirect(url_for('mail.index'))#el blueprint que cree con el nombre 'email'
        else:
            for error in errors:
                flash(error)
        
    return render_template('mails/create.html')


def send(to, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config('SENDGRID_KEY'))

