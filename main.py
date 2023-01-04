from flask import Flask,render_template
import requests
import pandas as pd

df=pd.read_csv("dictionary.csv")

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def translate(word):
    translation=str(df.loc[df['word']==word]['definition'].squeeze())
    return{
            "Translation": translation,
            "Word": word
        }

if __name__=="__main__":
    app.run(debug=True,port=5001)
