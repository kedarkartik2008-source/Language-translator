from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()

        text = data.get("text", "").strip()
        source = data.get("source", "auto")
        target = data.get("target", "en")

        if not text:
            return jsonify({
                "success": False,
                "message": "Please enter some text."
            })

        translated_text = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        return jsonify({
            "success": True,
            "translation": translated_text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Translation failed. Please check your internet connection."
        })


if __name__ == "__main__":
    app.run(debug=True)