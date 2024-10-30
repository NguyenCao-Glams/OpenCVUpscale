from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
from upscale import Upscale

app = Flask(__name__)

# Set the upload folder and allowed extensions
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('static/', '')
        
        # return f'Image uploaded successfully: {filename}'
        
        uscl = Upscale('models/EDSR_x4.pb', 'edsr', 4, filename)
        upscaled_image_path = uscl.upscale_image().replace('static/', '')
        
        return render_template(
            'upload.html',
            uploaded_image=uploaded_image_path,
            upscaled_image=upscaled_image_path
        )
    
    return 'File type not allowed'

if __name__ == '__main__':
    app.run(debug=True)