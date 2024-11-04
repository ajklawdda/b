from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template("index.html")


@app.route("/download-app/")
def download():
	return send_file("Прогноз погоды.exe")


if __name__ == '__main__':
	app.run(debug=True)
