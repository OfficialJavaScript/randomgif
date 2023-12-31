#!/usr/bin/env python3

from flask import Flask, render_template
from getgif import getimage

app = Flask(__name__)

@app.route("/")
def main():
    nokey = False
    image_url = getimage()
    if image_url == "nokey":
        nokey = True
        return render_template("index.html", image_url=image_url, nokey=nokey)
    return render_template("index.html", image_url=image_url, nokey=nokey)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)