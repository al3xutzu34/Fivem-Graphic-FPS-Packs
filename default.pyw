import shutil
import os
import getpass
import sys
import zipfile

#Pentru a beneficia de accesul la appdata
username = getpass.getuser()

cur_dir = os.getcwd()

#Cauta destinatia FiveM-ului
dst_path = "C:/Users/"+username+"/AppData/Local/FiveM/FiveM.app"

#shutil.copy(src_file, dst_path)

#Sterge citizenul pentru a instala ResourcePack-ul
mydir = dst_path+"/citizen"
shutil.rmtree(mydir)


########################### MADE BY HTTPS://YOUTUBE.COM/ALEXUTZUGAMING ###########################
########################### MADE BY HTTPS://YOUTUBE.COM/ALEXUTZUGAMING ###########################
########################### MADE BY HTTPS://YOUTUBE.COM/ALEXUTZUGAMING ###########################
########################### MADE BY HTTPS://YOUTUBE.COM/ALEXUTZUGAMING ###########################