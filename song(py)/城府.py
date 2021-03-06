import pickle
import os

class Song:
    def __init__(self):
        self.name=""
        self.singer=""
        self.style=""
        self.tune=[]

song=Song()
song.name="城府"
song.singer={"许嵩"}
song.style={}
song.tune=[
    ['Am',
     [6,6,7,1,1,1,3,3],
     [0,0,0,1,1,1,0,0]],
    ['Dm',
     [5,5,4,4,4,4,4,4],
     [0,0,0,0,0,0,0,0]],
    ['G',
     [5,5,6,7,7,7,2,2],
     [0,0,0,0,0,0,0,0]],
    ['C',
     [4,4,3,3,3,2,2,3],
     [0,0,0,0,0,0,0,0]],
    ['F',
     [4,4,4,4,5,4,4,5],
     [0,0,0,0,0,0,0,0]],
    ['Dm',
     [6,6,6,6,6,6,6,6],
     [0,0,0,0,0,0,0,0]],
    ['E',
     [7,7,1,7,7,7,1,2],
     [0,0,1,0,0,0,1,1]],
    ['E',
     [2,2,1,7,7,7,7,7],
     [1,1,1,0,0,0,0,0]],
    ['Am',
     [6,6,7,1,1,1,3,3],
     [0,0,0,1,1,1,0,0]],
    ['Dm',
     [5,5,4,4,4,4,4,4],
     [0,0,0,0,0,0,0,0]],
    ['G',
     [5,5,6,7,7,7,2,2],
     [0,0,0,0,0,0,0,0]],
    ['C',
     [4,4,3,3,3,2,2,3],
     [0,0,0,0,0,0,0,0]],
    ['F',
     [4,4,4,4,5,4,4,5],
     [0,0,0,0,0,0,0,0]],
    ['Dm',
     [6,6,6,6,6,6,6,6],
     [0,0,0,0,0,0,0,0]],
    ['E',
     [7,7,1,7,7,7,1,7],
     [0,0,1,0,0,0,1,0]],
    ['E',
     [7,7,1,7,7,7,7,7],
     [0,0,1,0,0,0,0,0]],
    ['Am',
     [3,3,6,6,6,6,6,6],
     [0,0,0,0,0,0,0,0]]]

file=open('城府.pkl','wb')
pickle.dump(song,file)
file.close()
