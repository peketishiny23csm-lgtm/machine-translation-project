from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        translated = translator.translate(text, src='en', dest='fr')
        result = translated.text
    return render_template("index.html", result=result)

import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))