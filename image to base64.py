import base64
import os

file_path = input('Enter file name with path\n')
filename,ext = os.path.splitext(file_path)
os.chdir(os.path.join(os.environ['userprofile'],'Desktop'))

with open(file_path,'rb') as image_file:
    image_b64 = base64.b64encode(image_file.read())
    ##print('file :'+file_path)
    ##print('date:image/'+ext+';base64,{}'.format(image_b64))
    ##print('-------------------------------------------------------')
    ##print('-------------------------------------------------------')
    with open('image_to_base64.txt','a+') as image_write:
        image_write.write('file :'+file_path)
        image_write.write('\ndate:image/'+ext.split('.')[1]+';base64,{}'.format(str(image_b64).split("'")[1]))
        image_write.write('\n-------------------------------------------------------')
        image_write.write('\n-------------------------------------------------------')


        
print('Converted image to base64 successfully!')
