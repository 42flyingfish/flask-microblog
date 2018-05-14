from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bob'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beutiful day by the beach!'},
            {
                'author': {'username': 'Alice'},
                'body': 'Exams are tomorrow!'}
            ]

    return render_template('index.html', title='Home', user=user, posts=posts) 
