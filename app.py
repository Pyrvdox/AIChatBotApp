from flask import Flask, render_template, request, session
from aichat import conversation_handler
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "veeeeery_important_hehe")

@app.route("/", methods=["GET", "POST"])           
def home():
    history = session.get("history", [])

    if request.method == "GET":
        return render_template("index.html") 
              
    if request.method == "POST":
        user_input = request.form["message"]
        history.append(("user", user_input))

        conversation_context = "\n".join(f"{person}: {text}" for person, text in history)
        print(conversation_context)

        bot_response = conversation_handler(conversation_context, user_input)
        print(bot_response)

        history.append(("bot", bot_response))

        session["history"] = history

        return render_template("index.html", history=history)   

if __name__ == "__main__":
    app.run(debug=True) 

