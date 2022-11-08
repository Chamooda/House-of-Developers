import hashlib
from PIL import Image

def Encrypt(img):
        
    imag = Image.open(f"{img}","r")
    rgba = imag.convert('RGBA')
    pix = list(rgba.getdata())
    hash = ""
    #print(pix)


    for i in pix:
        da_string = str(i[0])+str(i[1])+str(i[2])+str(i[3])+"-"
        hash = hash + da_string
        hash  = hashlib.sha256(hash.encode()).hexdigest()


    return hash












#pip install pillow

#b5769c5c9004af8b6d94c0498f65cf22eee1f6d990029a7700e24db300c33b47
#396716e99b297015fbb67e9e1ae99dfceeb115f6324e4f112b31e008065443d0
#6956d8662b9e4014d9c9d7fa44b0c906347fae561d6b2b5a5da583e7e6ff1e2a
# imag = Image.open("bird 3.png","r")
# rgba = imag.convert('RGBA')
# pix = list(rgba.getdata())
# hash = ""
# da_real_hash= ""
# prevhash = ""
# print(pix)


# for i in pix:
#     da_string = str(i[0])+str(i[1])+str(i[2])+str(i[3])+"-"
#     hash = hash + da_string
#     hash  = hashlib.sha256(hash.encode()).hexdigest()


# print(hash)












#pip install pillow

#b5769c5c9004af8b6d94c0498f65cf22eee1f6d990029a7700e24db300c33b47
#396716e99b297015fbb67e9e1ae99dfceeb115f6324e4f112b31e008065443d0
#6956d8662b9e4014d9c9d7fa44b0c906347fae561d6b2b5a5da583e7e6ff1e2a