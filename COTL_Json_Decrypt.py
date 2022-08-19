import io
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import json



Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

try:
    with open(filename, "rb+") as f:
        byte = f.read(1)
        print(byte)
        if(byte.decode("utf-8") == 'E'):
            print("Valid save file... continuing.")
            key = f.read(16)
            print(key)
            iv = f.read(16)
            print(iv)


            cipher = AES.new(key,AES.MODE_CBC,iv)
            jsonObj = json.loads(unpad(cipher.decrypt(f.read()), AES.block_size))
            jsonFormatted = json.dumps(jsonObj,indent=2)
            print(jsonFormatted)

            f.seek(0)
            f.write(jsonFormatted.encode("utf-8"))

            print("Done!")

        else:
            print("Invalid save file / corrupted")
except IOError:
     print('Error While Opening the file!')

print("Press enter to continue")
input()
