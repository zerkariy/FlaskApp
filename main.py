from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

menu = ['это',"вот это","и это", "dadadsda"]


@app.route('/')
def greeting():
  return render_template('hello.html', name="User")

@app.route('/index')
def index():
  print(url_for('index'))
  return render_template('index.html', menu=menu)

@app.route('/about')
def about():
  print(url_for('about'))
  return render_template('about.html', title='jopa', menu=menu)



if __name__ == '__main__':
  app.run(debug=True) # debug true задаем специально для разработки (в данном случае при обновление/изменение кода приложение автоматически само обновит данные на сайте)