import flask

app = flask.Flask(__name__)


def mock_sample_data():
    return [
        {'name': 'test', 'version': '1.2.3'},
        {'name': 'test2', 'version': '3.2.1'},
    ]


@app.route('/')
def index():
    sample_data = mock_sample_data()
    return flask.render_template('index.html', data=sample_data)


if __name__ == '__main__':
    app.run(debug=True)
