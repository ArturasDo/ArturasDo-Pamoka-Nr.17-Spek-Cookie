import random
# import sys
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")  # check if there is already a cookie named secret_number

    response = make_response(render_template("index.html"))
    if not secret_number:  # if not, create a new cookie
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = (request.form.get("guess"))
    if guess.upper() == "C":
        # message = "Thank you. Your game is over."
        message = "Ačiū. Žaidimo pabaiga."
        response = make_response(render_template("result.html", message=message))
        return response
    if guess.isdigit():
        pass
    else:
        message = "Jūs įvedėte raides. Pakartokite."
        response = make_response(render_template("result.html", message=message))
        return response

    guess = int(guess)
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Sveikiname. Slaptas skaičius yra {0}".format(str(secret_number))
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))  # set the new secret number
        return response
    elif guess > secret_number:
        message = "Bandykite mažesnį skaičių."
        return render_template("result.html", message=message)
    elif guess < secret_number:
        message = "Bandykite didesnį skaičių."
        return render_template("result.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)