from flask import Flask, render_template, request, redirect
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", fr = friends)
@app.route("/newform")
def newform():
    friends = Friend.get_all()
    print(friends)
    return render_template("form.html")
    
@app.route('/create_friend', methods=["GET","POST"])
def create_friend():
    if request.method == "POST":
        data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
        Friend.save(data)
        return redirect('/')
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)