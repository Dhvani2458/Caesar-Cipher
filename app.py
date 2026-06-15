from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

HISTORY_FILE = "history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def caesar_cipher(text, shift, encrypt=True):
    result = ""

    if not encrypt:
        shift = -shift

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cipher")
def cipher():
    return render_template("cipher.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/working")
def working():
    return render_template("working.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    message = data.get("message", "")
    shift = int(data.get("shift", 3))
    action = data.get("action")

    if action == "encrypt":
        result = caesar_cipher(message, shift, True)
        act = "Encrypt"
    else:
        result = caesar_cipher(message, shift, False)
        act = "Decrypt"

    history = load_history()

    history.insert(0, {
        "message": message,
        "shift": shift,
        "action": act,
        "result": result,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    history = history[:25]
    save_history(history)

    return jsonify({
        "result": result,
        "status": f"{act}ed successfully"
    })


@app.route("/get_history")
def get_history():
    return jsonify(load_history())


@app.route("/clear_history")
def clear_history():
    save_history([])
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)