from flask import Blueprint, request, render_template
from flask.globals import g

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET', 'POST'])
def index():
    global sentence
    sentence = []
    return render_template('/main/index.html')

@main.route('/search/', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        character = request.form['character']
        g.character = character

        global sentence
        sentence = []

        f = open("./app/main/nwood.txt", "rt", encoding='UTF8')
        lines = f.readlines()

        for l in lines:
	        rs = l.rstrip()
	        if character in rs:
		        sentence.append(rs)

    return render_template('/search/index.html', character=character, len=len(sentence), sentence=sentence)