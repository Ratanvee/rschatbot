from flask import Flask, render_template, request, jsonify
import chatbot

app = Flask(__name__)



# Simple chatbot response logic (can be extended)
def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm just a simple chatbot. I don't understand that yet."

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle chatbot messages
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form.get("message")
    # bot_reply = chatbot_response(user_message)
    bot_reply = chatbot.output(user_message)
    print("This is bot replay : ",bot_reply)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
