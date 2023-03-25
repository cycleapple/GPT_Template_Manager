import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    prompt = db.Column(db.String(200), nullable=False)
    prompt_description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Block %r>' % self.title

# create the tables in the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    blocks = Block.query.all()
    return render_template('index.html', blocks=blocks)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        prompt = request.form['prompt']
        prompt_description = request.form['prompt_description']
        block = Block(title=title, prompt=prompt, prompt_description=prompt_description)
        db.session.add(block)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    block = Block.query.get_or_404(id)
    if request.method == 'POST':
        block.title = request.form['title']
        block.prompt = request.form['prompt']
        block.prompt_description = request.form['prompt_description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', block=block)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    block = Block.query.get_or_404(id)
    db.session.delete(block)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
