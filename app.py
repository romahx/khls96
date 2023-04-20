from flask import Flask, render_template, request, json, flash
from models import InputData, db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


menu = [
    {'name': 'Добавить данные', 'url': 'index'},
    {'name': 'Список записей', 'url': 'list'}]


@app.route('/index', methods=['GET', 'POST'])
@app.route('/')
def index():
    if request.method == 'POST':
        coins = 0
        for k in range(len(request.form)):
            n = 'name'+str(k)
            if len(request.form.get(n)) != 0:
                jsons = json.dumps(request.form.get(n), ensure_ascii=False)
                db.create_all()
                db.session.add(InputData(name=jsons))
                db.session.commit()
            else:
                coins += 1
                continue
        if coins > 0:
            flash('Незаполненные инпуты не добавлены в БД', category='error')
        else:
            flash('Форма отправлена', category='success')
    return render_template('index.html', title='Добавление данных', menu=menu)


@app.route('/list')
def all_records():
    jsons_list = InputData.query.all()
    return render_template('list.html', title='Список данных', menu=menu, jsons_list=jsons_list)


if __name__ == '__main__':
    app.run(debug=True)
