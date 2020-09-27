'''
Created on 24.03.2015

@author: Jochen Weiss
'''

from __future__ import print_function
import os
import sys
import platform

if __name__ == '__main__':
    pass

def check_dir(direc):
    '''
    check the directory for mp3,
    ogg, ,flac, and m3u files
    @param direc directory where the search starts
    '''
    found_m3u = False
    found_music_files = []
    for filename in os.listdir(direc):
        if((filename.find('.mp3') > 0) or (filename.find('.MP3') > 0)):
            found_music_files.append(filename)
            print ('MP3: '+filename)
        elif((filename.find('.ogg') > 0) or (filename.find('.OGG') > 0)):
            found_music_files.append(filename)
            print ('OGG: '+filename)
        elif((filename.find('.flac') > 0) or (filename.find('.FLAC') > 0)):
            found_music_files.append(filename)
            print ('FLAC: '+filename)
        elif((filename.find('.m4a') > 0) or (filename.find('.M4A') > 0)):
            found_music_files.append(filename)
            print ('FLAC: '+filename)
        elif((filename.find('.m3u') > 0) or (filename.find('.M3U') > 0)):
            found_m3u = True
            print ('found_m3u: '+ filename)
        
        print (filename)

    found_music_files.sort()
    l_fmf = len(found_music_files)
    if (not found_m3u and l_fmf > 0):
        print('###################################')
        a_help = ""
        if platform.system().find('Linux') > -1:
            a_help = direc.rfind('/')
        else:
            a_help = direc.rfind('\\') # on Windows
        directory_name = direc[a_help+1:]
        print(directory_name)
        fil = open(direc+"/"+directory_name+".m3u", "w")


        for music in found_music_files:
            print(music)
            fil.write(music+'\n')
        fil.close()

START_DIR = sys.argv[1]
START_DIR = os.path.abspath(START_DIR)
print(START_DIR)
for dirname, dirnames, filenames in os.walk(START_DIR):
    for subdirname in dirnames:
        print ("FOUND DIRECTORY: ", os.path.join(dirname, subdirname))
        check_dir(os.path.join(dirname, subdirname))
