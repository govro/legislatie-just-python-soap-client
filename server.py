from flask import Flask, render_template, request
from client import LegislatieJustClient

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/search", methods=['POST'])
def search():
    client = LegislatieJustClient()
    params = {v: request.form[v] for k, v in enumerate(request.form)}
    results = client.search(params).Legi
    return render_template('search.html', laws=results)

if __name__ == "__main__":
    app.run(debug=True)
