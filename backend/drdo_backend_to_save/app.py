from flask import Flask, request, jsonify, render_template
import langchain_sql_assistant  # ✅ Importing your file as a module

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    question = request.json.get("question")

    try:
        result = langchain_sql_assistant.get_answer(question)  # ✅ We’ll define this function
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": f"❌ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
