import os
from main import app

# Fix the upload folder path for Windows
current_dir = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(current_dir, 'files')
os.makedirs(upload_folder, exist_ok=True)
app.config['UPLOAD_FOLDER'] = upload_folder

if __name__ == "__main__":
    print(f"Serving on http://0.0.0.0:5000")
    print(f"Files will be stored in: {upload_folder}")
    app.run(host="0.0.0.0", port=5000)