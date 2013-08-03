from flask import Flask
app = Flask(__name__, static_url_path='/', static_folder='html')

@app.route("/api")
def html():
    return "Works!"





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)