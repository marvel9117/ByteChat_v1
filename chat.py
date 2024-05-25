#!/usr/bin/python3
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"
socketio = SocketIO(app)

#to store our rooms so as to check if it exists
rooms = {}


def generate_unique_code(length):
    while True:
        code = ""
        for i in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code

@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        #check if user pass a name
        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)

        #check if attempting to join a room without code
        if join != False and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)

        #check what room user is going to and if it exist
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
             return render_template("home.html", error="Rooms does not exist.", code=code, name=name)

         #store information about the user / store data in a section intead of autentication
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template("home.html")


@app.route("/room")
def room():
    return reander_template("room.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)
