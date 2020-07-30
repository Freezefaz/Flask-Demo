import json
# give unique id
import uuid

# Don't leave a json file with empty if not cannot open
# Make sure the file is has {}
database = {}


def save():
    # not necessary but as a precaution
    global database
    print(database)
    with open('db.json', 'w') as filehandler:
        json.dump(database, filehandler)

def load():
    global database
    with open("db.json", "r") as fileptr:
        database = json.load(fileptr)  # to refer to the global database

# access to images in gallery
def get_database():
    global database
    return database

# to add image and info into gallery database
def put(asset_id, url, caption):
    global database
    # extract unique id, DON'T USE INFO FROM IMAGES COZ IT CHANGES WITH EACH UPLOAD
    image_id = str(uuid.uuid1())
    # make it into a dictionary
    image = {
        "id": image_id,
        "asset_id": asset_id,
        "url": url,
        "caption": caption
    }
    # give each image a unique id
    database[image_id] = image

# update image in the gallery database
def update(image_id, asset_id, url, caption):
    global database
    image = {
        "id": image_id,
        "asset_id": asset_id,
        "url": url,
        "caption": caption
    }
    database[image_id] = image

# get individual image
def get_image(asset_id):
    global database
    return database[asset_id]
