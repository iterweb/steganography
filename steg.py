import os
import zipfile
from time import sleep

check_os = os.name

image_format = (('.jpg', '.jpeg', '.png'), ('arcHIvE.zip', 'steg.exe', 'steg.py'),)

my_zip = zipfile.ZipFile('arcHIvE.zip', 'w')


for file in os.listdir():
    if file.endswith(image_format[0]):
        img = file
        new_img = 'new_' + img
    if not file.endswith(image_format[0] + image_format[1]):
        my_zip.write(os.path.join(file), compress_type=zipfile.ZIP_DEFLATED)
my_zip.close()


if check_os == 'nt':
    print('OS Windows')
    sleep(5)
    os.system('copy /b %s + arcHIvE.zip %s' % (img, new_img))
    os.remove('arcHIvE.zip')
    print('ГОТОВО')
    sleep(3)

if check_os == 'posix':
    print('OS Linux')
    sleep(5)
    os.system('cat %s arcHIvE.zip > %s' % (img, new_img))
    os.remove('arcHIvE.zip')
    print('ГОТОВО')
    sleep(3)
