from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Railway PaaS!</h1><p>Tugas PaaS berhasil online.</p>"

if __name__ == "__main__":
    app.run()
