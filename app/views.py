"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, forms
from flask import render_template, request, redirect, url_for, flash

from app import mail
from flask_mail import Message

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.roue('/contact', methods=('GET', 'POST'))
def contact():
    form = forms.ContactForm()
    if form.validate_on_submit() and  request.method == 'POST':
        msg = Message(form.subject.data, sender=(form.name.data, form.email.data), recipients=[
            "4176872f43-187af3@inbox.mailtrap.io"
        ])
        msg.body=form.message.data
        mail.send(msg)
        flash('Your message has been sent!')
        return redirect(url_for('home.html', mailed=True))
        
    elif request.method == 'POST':
        return render_template('contact.html', form=form, invalid=True)
    return render_template('contact.html', form=form, invalid=False)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
