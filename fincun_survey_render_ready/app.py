from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        email = request.form["email"]
        phone = request.form["phone"]
        need = request.form["need"]
        return render_template("thankyou.html", name=name, need=need)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
