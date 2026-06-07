from flask import Flask, request, send_file, jsonify
import io
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Background Remover API çalışıyor"})

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return jsonify({"error": "Görsel bulunamadı"}), 400

    try:
        # Lazy load - sadece gerektiğinde import et
        from rembg import remove
        
        file = request.files["image"]
        input_data = file.read()
        
        # Hafif model ile işle (u2netp en hafif model)
        output_data = remove(input_data, model_name="u2netp")
        
        return send_file(
            io.BytesIO(output_data),
            mimetype="image/png",
            as_attachment=False
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)