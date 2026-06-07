from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Background Remover API çalışıyor"})

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return jsonify({"error": "Görsel bulunamadı"}), 400

    file = request.files["image"]
    input_data = file.read()

    output_data = remove(input_data)

    return send_file(
        io.BytesIO(output_data),
        mimetype="image/png",
        as_attachment=False
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)