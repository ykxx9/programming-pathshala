from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "OK"}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4040, debug=True)