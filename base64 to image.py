import base64
import os

base64_str = input('Enter base64 string\n')

os.chdir(os.path.join(os.environ['userprofile'],'Desktop'))

filename = 'Image.'+base64_str.split(';')[0].split('/')[1]
with open(filename,'wb') as image_write:
    image_write.write(base64.b64decode(base64_str.split(',')[1]))

print('Convert base64 to image successfully!')
