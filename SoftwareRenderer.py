from gl import *


# Desplegar resultado
# Referencia: https://www.geeksforgeeks.org/python-pil-image-show-method/
from PIL import Image


def Proyecto1(filename):
    r = Render(1920, 1080)

    # Fondo
    r.glBackground("models/fondo.bmp")

    # ------------------ 1 ------------------

    r.glLookAt(V3(0, -20, -20), V3(0, -10, 0))

    r.shaderUsed = Shader.treeShading
    r.glModel(
        "models/arbol.obj",
        translation=V3(-35, -65, -105),
        scalationFactor=V3(2.3, 2.3, 2.3),
    )
    r.shaderUsed = Shader.renoShading
    r.glModel(
        "models/reno.obj",
        translation=V3(21, -23, -65),
        scalationFactor=V3(2.3, 2.3, 2.3),
        rotation=V3(5, 0, 0),
    )

    r.shaderUsed = Shader.flatShading
    r.textureUsed = Texture("models/galletitas.bmp")
    r.glModel(
        "models/galletitas.obj",
        translation=V3(-15, -95, -95),
        scalationFactor=V3(4.5, 4.5, 4.5),
        rotation=V3(0, 0, 0),
    )

    r.shaderUsed = Shader.flatShading
    r.textureUsed = Texture("models/santa.bmp")
    r.glModel(
        "models/santa.obj",
        translation=V3(13, -85, -95),
        scalationFactor=V3(190, 190, 190),
        rotation=V3(0, 0, 0),
    )

    r.shaderUsed = Shader.flatShading
    r.textureUsed = Texture("models/banca.bmp")
    r.glModel(
        "models/bench.obj",
        translation=V3(30, -60, -95),
        scalationFactor=V3(7, 7, 7),
        rotation=V3(0, 0, 0),
    )

    filename = filename + ".bmp"

    r.glFinish(filename)
    im = Image.open(filename)
    im.show()
