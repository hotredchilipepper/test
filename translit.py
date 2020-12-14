from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/a', methods=['POST','GET'])
def create_text():
    if request.method == "POST":
        text = request.form['name']
    else:
        return render_template("index.html")

def translit(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|h|tc|ch|sh|shch||y||e|iu|ia'.split(
        '|')
    tab = {k: v for k, v in zip(cyrillic, latin)}
    newtext: str = ''
    for ch in text:
        func = str.capitalize if ch.isupper() else str.lower
        newtext += func(tab.get(ch.lower(), ch))
    return newtext



if __name__ == '__main__':
    app.run(debug=True)

