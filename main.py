from flask import render_template, Flask, url_for

app = Flask(__name__)

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('profs.html', prof=prof)



@app.route('/list_prof/<param>')
def list_prof(param):
    return render_template('list.html', param=param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.3')
