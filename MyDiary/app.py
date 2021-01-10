import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for

from init_db import Database

db = Database()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        from flask import abort
        abort(404)
    return post


app = Flask(__name__)
# SECRET_KEY required for session, flash and Flask Sqlalchemy to work
app.config['SECRET_KEY'] = 'xyz1234'


# index route, shows index.html view
@app.route('/')
def index():
    return render_template('index.html')


# login route, shows login.html view
@app.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('index.html')


# about route, shows about.html view
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<int:post_id>')
def post(post_id):
    _post = get_post(post_id)
    return render_template('event.html', post=_post)


@app.route('/view_all')
def view_all():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('viewAll.html', posts=posts)


@app.route('/add_event', methods=('GET', 'POST'))
def add_event():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            flash('Event added successfully')
            return redirect(url_for('index'))
    return render_template('addEvent.html')


# run Flask app in debug mode
db.__init__()
app.run(debug=True)
