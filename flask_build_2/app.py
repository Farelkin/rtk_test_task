from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    res, num = 0, 0
    response = 'no data'
    if request.method == "POST":
        content_text = request.form['text']
        content_text = str(content_text).replace(',', '.').replace('b', '').replace("'", '')
        content_text_list = content_text.split(' ')
        for val in content_text_list:
            if len(content_text_list) == 2:
                try:
                    num = int(val)
                except ValueError:
                    print('Нужны два числа')
                    return 'Нужны два числа'
                res += num
            else:
                return 'Дано больше двух чисел или ни одного или всего лишь одно'
        print(res)
        response = f'sum between {content_text} is: {str(res)}'

    return response


if __name__ == '__main__':
    app.run()
