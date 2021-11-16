import flask
import pandas as pd
from joblib import dump, load


with open(f"model/model.joblib", 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        marka = flask.request.form['Марка']
        car_model = flask.request.form['Модель']
        year = flask.request.form['Год выпуска']
        kuzov = flask.request.form['Кузов']
        color = flask.request.form['Цвет']
        korobka = flask.request.form['Коробка']
        role = flask.request.form['Руль']
        condition = flask.request.form['Состояние']
        dvigatel = flask.request.form['Тип двигателя']
        n_peredach = flask.request.form['Кол-во передач']
        n_doors = flask.request.form['Количество дверей']
        n_seats = flask.request.form['Количество мест']
        fuel = flask.request.form['Объем']
    
        input_variables = pd.DataFrame([[marka, car_model,year, kuzov,  color,korobka,role, condition,  dvigatel,n_peredach, n_doors, n_seats,fuel]],
                                       columns=['Марка','Модель','Год выпуска','Кузов','Цвет','Коробка','Руль', 'Состояние', 'Тип двигателя',
                                                'Кол-во передач','Количество дверей','Количество мест','Объем'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('index.html', original_input={'Марка': marka,'Модель': car_model,'Год выпуска': year, 'Кузов': kuzov, 'Цвет':  color,'Коробка': korobka,'Руль': role,'Состояние': condition, 'Тип двигателя': dvigatel, 'Кол-во передач': n_peredach,'Количество дверей': n_doors,'Количество мест': n_seats,'Объем':fuel},
                                     result=predictions)

@app.route('/about/')
def about():
    return flask.render_template('about.html')

@app.route('/contact/')
def contacts():
    return flask.render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
