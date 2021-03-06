import pickle
import os

class Song:
    def __init__(self):
        self.name=""
        self.singer=""
        self.style=""
        self.tune=[]

song=Song()
song.name="星河万里"
song.singer={"苏贝贝"}
song.style={}
song.tune=[
    ['Am',
     [3,3,2,3,3,3,1,1],
     [0,0,0,0,0,0,1,1]],
    ['Em',
     [7,1,7,6,7,7,3,3],
     [0,1,0,0,0,0,0,0]],
    ['F',
     [6,5,6,1,6,5,3,2],
     [0,0,0,1,0,0,0,0]],
    ['C',
     [3,5,5,3,3,3,3,3],
     [0,0,0,0,0,0,0,0]],
    ['Am',
     [3,3,2,3,3,3,1,1],
     [0,0,0,0,0,0,1,1]],
    ['C',
     [2,2,1,7,7,7,5,6],
     [1,1,1,0,0,0,0,0]],
    ['F',
     [6,6,6,6,6,6,6,6],
     [0,0,0,0,0,0,0,0]],
    ['Em',
     [6,7,1,1,7,7,7,7],
     [0,0,1,1,0,0,0,0]],
    ['Am',
     [3,3,2,3,3,3,1,1],
     [0,0,0,0,0,0,1,1]],
    ['Em',
     [7,1,7,6,7,7,3,3],
     [0,1,0,0,0,0,0,0]],
    ['F',
     [6,5,6,1,6,5,3,2],
     [0,0,0,1,0,0,0,0]],
    ['C',
     [3,5,5,3,3,3,3,3],
     [0,0,0,0,0,0,0,0]],
    ['Am',
     [3,3,2,3,3,3,1,1],
     [0,0,0,0,0,0,1,1]],
    ['C',
     [2,2,1,7,7,7,5,6],
     [1,1,1,0,0,0,0,0]],
    ['F',
     [6,6,6,6,6,6,6,6],
     [0,0,0,0,0,0,0,0]],
    ['Em',
     [1,7,6,5,5,6,7,6],
     [1,0,0,0,0,0,0,0]],
    ['F',
     [6,6,6,6,6,6,6,6],
     [0,0,0,0,0,0,0,0]]]

file=open('星河万里.pkl','wb')
pickle.dump(song,file)
file.close()
