from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.comments import Comment
from forms.add_comment_form import CommentForm
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/<string:id>")
def return_comments(id):
    db_sess = db_session.create_session()
    comments = db_sess.query(Comment).filter(Comment.object_id == id).all()
    ans = []
    for i in comments:
        ans.append({i.title: i.content})
    print(ans)
    return json.dumps(ans, ensure_ascii=False).encode('utf8')


@app.route("/add_comment/<string:id>",  methods=['GET', 'POST'])
def add_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        comment = Comment()
        comment.title = form.title.data
        comment.content = form.content.data
        comment.object_id = id
        db_sess.merge(comment)
        db_sess.commit()
        return redirect('/thanks')
    return render_template('load_comment.html', title='Добавление комментария',
                           form=form)


@app.route("/thanks")
def thanks():
    return render_template('thanks.html')


def main():
    db_session.global_init("db/comments.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()