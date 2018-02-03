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
    check the directory mp3,
    ogg, and msu files
    @param direc directory where the search starts
    '''
    found_m3u = False
    foundMusicFiles = []
    for filename in os.listdir(direc):
        if((filename.find('.mp3') > 0) or (filename.find('.MP3') > 0)):
            foundMusicFiles.append(filename)
            print ('MP3: '+filename)
        elif((filename.find('.ogg') > 0) or (filename.find('.OGG') > 0)):
            foundMusicFiles.append(filename)
            print ('OGG: '+filename)
        elif(filename.find('.m3u') > 0 or filename.find('.M3U')):
            found_m3u = True
            print ('found_m3u: '+ filename)
        print (filename)

    foundMusicFiles.sort()
    if (not found_m3u and (len(foundMusicFiles) > 0)):
        print('###################################')
        a = ""
        if platform.system().find('Linux') > -1:
            a = direc.rfind('/')
        else:
            a = direc.rfind('\\') # on Windows
        directoryName = direc[a+1:]
        print(directoryName)
        fi = open(direc+"/"+directoryName+".m3u", "w")


        for music in foundMusicFiles:
            print(music)
            fi.write(music+'\n')
        fi.close()

startDir = sys.argv[1]

for dirname, dirnames, filenames in os.walk(startDir):
    for subdirname in dirnames:
        print ("FOUND DIRECTORY: ", os.path.join(dirname, subdirname))
        check_dir(os.path.join(dirname, subdirname))
