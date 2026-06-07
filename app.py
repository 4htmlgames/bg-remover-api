from flask import Flask, request, send_file, jsonify
from transparent_background import Remover
from PIL import Image
import io

app = Flask(__name__)

# Modeli başlangıçta yükle
remover = Remover(mode='base-nightly')

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Background Remover API çalışıyor"})

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return jsonify({"error": "Görsel bulunamadı"}), 400

    try:
        file = request.files["image"]
        img = Image.open(file).convert("RGB")
        
        output = remover.process(img, type='rgba')
        
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        buf.seek(0)
        
        return send_file(buf, mimetype="image/png", as_attachment=False)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)