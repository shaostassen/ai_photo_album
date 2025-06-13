from flask import Flask, send_from_directory, render_template
import os

# CONFIG
PHOTO_DIR = "/home/shao_stassen/photos"  # Folder where photos are stored
ALLOWED_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".heic"}

app = Flask(__name__)

def list_images():
    image_paths = []
    for root, dirs, files in os.walk(PHOTO_DIR):
        for filename in files:
            if any(filename.lower().endswith(ext) for ext in ALLOWED_EXTS):
                rel_path = os.path.relpath(os.path.join(root, filename), PHOTO_DIR)
                image_paths.append(rel_path)
    return sorted(image_paths)

@app.route("/images/<path:filename>")
def get_image(filename):
    return send_from_directory(PHOTO_DIR, filename)

@app.route("/")
def slideshow():
    images = list_images()
    return render_template("slideshow.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
