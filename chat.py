#!/usr/bin/python3
from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, debug=True)
