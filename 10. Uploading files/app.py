from flask import Flask, render_template, request, redirect, url_for
import os
import gallery

# allow us to read in the variables from our .env files
from dotenv import load_dotenv
load_dotenv()

# to get the values from .env file
# In caps as this is convention to indicate that the values are from another environment
CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')

app = Flask(__name__)

# Load everytime the functions is done
gallery.load()

# to display all the uploaded images at page
@app.route('/')
def display_gallery():
    images = gallery.get_database()
    return render_template('gallery.template.html', images=images)

# page for widget to pop up and upload stuff
# everytime upload need to include the cloud stuff
@app.route('/upload-image')
def display_upload_route():
    return render_template('layout.template.html', cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)

# page to edit image
# everytime upload need to include the cloud stuff
@app.route('/edit-image/<image_id>')
def edit_image(image_id):
    # to get image from gallery
    image = gallery.get_image(image_id)
    return render_template('edit_image.template.html', cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET, image=image)

# page to edit image
@app.route('/edit-image/<image_id>', methods=["POST"])
def process_edit_image(image_id):
    # get info from the form
    caption = request.form.get('caption')
    url = request.form.get('uploaded-file-url')
    asset_id = request.form.get('asset-id')
    gallery.update(image_id, asset_id, url, caption)
    return "image upated"

# page for widget to pop up and upload stuff
@app.route('/upload-image', methods=["POST"])
def process_upload():
     # get info from the form
    caption = request.form.get('caption')
    url = request.form.get('uploaded-file-url')
    asset_id = request.form.get('asset-id')
    gallery.put(asset_id, url, caption)
    # Add to gallery
    gallery.save()
    return "image added"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
