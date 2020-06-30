import os
from ftplib import FTP
from keys import server_pass
ftp = FTP('files.000webhost.com')
ftp.login(user='sakshambhushan', passwd = server_pass)
ftp.cwd('/public_html/intrusion_detection/')
print('logged in to ftp')
def placeFile(filename):

    #filename = 'exampleFile.txt'

    ftp.storbinary('STOR '+os.path.basename(filename), open(filename, 'rb'))
    print('upload complete!')
    ftp.quit()

#placeFile()
