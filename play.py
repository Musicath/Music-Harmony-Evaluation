from tool import *
import pickle
import time
songs=[]
for i in os.listdir('song'):
    file = open('song' + os.sep + i, 'rb')
    song = pickle.load(file)
    file.close()
    songs.append(song)
#songs = Tune_Init(songs)
for song in songs:
    print(song.name)
    Play(song.tune)
    time.sleep(30)
