from flask import Flask,render_template
import requests


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def translate(word):
    response=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data=response.json()
    translation=data[0]['meanings'][0]['definitions'][0]['definition']
    return{
            "Translation": translation,
            "Word": word
        }

if __name__=="__main__":
    app.run(debug=True,port=5001)
