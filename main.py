import io
import qrcode
from base64 import b64encode
import eel

eel.init('web')


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}


@eel.expose
def generate_qr(data):
    img = qrcode.make(data)
    type(img)
    buffers = io.BytesIO()
    img.save(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")
    return "data:image/png;base64, " + encoded


eel.start('index.html', size=(1000, 600))
