from flask import Flask, render_template,request,redirect
# importar la clase de friend.py
from users import User
app = Flask(__name__)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    return render_template("index.html",users=users)
            


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/")

@app.route("/addUsers")
def addUsers():
    return render_template("addUsers.html")

if __name__ == "__main__":
    app.run(debug=True)