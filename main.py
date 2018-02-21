import requests, pprint, chaves, numpy as np, matplotlib.pyplot as plt, matplotlib.patches as patches
from PIL import Image

subscription_key = chaves.face_detection_api
assert subscription_key
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }

def request_image(image_loc):
    image_path = "images/" + image_loc
    image = open(image_path, "rb").read()
    response = requests.post(url=face_api_url, headers=headers, data=image)
    faces = response.json()
    print("We found: %d"%len(faces))
    #pprint.pprint(faces, indent=4)
    im = np.array(Image.open(image_path), dtype=np.uint8)
    fig,ax = plt.subplots(1)
    ax.imshow(im)
    if len(faces) > 0:
        for face in faces:
            y = int(face['faceRectangle']['top'])
            x = int(face['faceRectangle']['left'])
            z = int(face['faceRectangle']['height'])
            f = int(face['faceRectangle']['width'])
            rect = patches.Rectangle((x,y),z,f,linewidth=2,edgecolor='b',facecolor='none')
            ax.add_patch(rect)
    plt.savefig('rendered/' + image_loc)
    return 'rendered/' + image_loc
