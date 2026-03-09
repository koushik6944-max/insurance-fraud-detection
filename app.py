from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    claim = float(request.form["claim"])
    age = float(request.form["age"])
    previous = float(request.form["previous"])

    # simple fraud logic
    if claim > 15000 and previous > 2:
        result = "⚠️ Fraud Detected"
    else:
        result = "✅ Genuine Claim"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)