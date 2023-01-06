from base import Problem
import requests
import cv2

p = Problem(name='reading_qr')

img_url = p.get_question()['image_url']


img_data = requests.get(img_url).content
with open('qr.png', 'wb') as handler:
    handler.write(img_data)
    img=cv2.imread("qr.png")
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    body = {"code":val}
    p.send_answer(body)
