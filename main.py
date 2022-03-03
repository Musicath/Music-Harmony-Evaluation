import numpy as np
from definition import Song, Music
from read import songs
from tool import *
import pickle as pkl

debug = False
Num = 8  # 生成的旋律数

StrongHarmony = np.zeros((8, 36), dtype=float)#H(和弦,重音)
WeakHarmony = np.zeros((8, 36), dtype=float)#H(和弦,重音)
# 从左到右分别是：轻音，轻音前后的两个重音
FluencyTable = np.zeros((25, 25), dtype=float)#F(上一个重音,下一个重音)=轻音
file=open('HarmonyLambda.pkl','rb')
h = pkl.load(file)
file.close()#导入和谐度参数

def White(k):
    if k%12==1:
        return False
    elif k%12==3:
        return False
    elif k%12==6:
        return False
    elif k%12==8:
        return False
    elif k%12==10:
        return False
    else:
        return True

def Note5(k):
    if White(k):
        if k%12==5:
            return False
        elif k%12==11:
            return False
        else:
            return True
    else:
        return False

def Calculate():
    for i in range(1,8):
        chord_dig=Chord_Dig(Level_Chord(i))
        for j in chord_dig:
            for k in range(36):
                if (k-j)%12==0 and Note5(k):
                    StrongHarmony[i][k]=HNN(chord_dig[0],k,h)
                if HNN(chord_dig[0],k,h)>h[0]/2 and White(k):
                    WeakHarmony[i][k]=HNN(chord_dig[0],k,h)
    for song in songs:
        TuneList = []
        for t in song.tune:
            for i in range(8):
                TuneList.append([Chord_Level(t[0]),t[1][i]+(t[2][i]+1)*12])
        TuneLen=len(TuneList)
        for i in range(1,TuneLen-1,2):
            FluencyTable[TuneList[i+1][1]+12-TuneList[i-1][1]][TuneList[i][1]+12-TuneList[i-1][1]]+=1
    FluencyTable[0][0]/=2
    if debug:
        np.set_printoptions(formatter={'int': '{:d}'.format})
        print("Below: HarmonyTable")
        print(HarmonyTable)
        print("Below: FLuencyTable")
        print(FLuencyTable)


def sigmoid(X):
    return 1.0 / (1 + np.exp(-float(X)))


def normalization1(Dic):  # 计算概率
    dic = np.array(Dic, np.float32)
    if np.sum(dic[:]) != 0.0:
        dic[:] = pow(dic[:],1)
        dic[:] = dic[:] / np.sum(dic[:])
    else:
        n = dic.shape[0]
        for i in range(n):
            dic[i] = 1 / n
    return dic


def normalization2(Dic):  # 计算概率
     dic = np.array(Dic, np.float32)
     if np.sum(dic[:, :]) != 0.0:
         dic[:, :] = dic[:, :] / np.sum(dic[:, :])
     return dic


def normalization3(Dic):  # 计算概率
    dic = np.array(Dic, np.float32)
    if np.sum(dic[:, :, :]) != 0.0:
        dic[:, :, :] = dic[:, :, :] / np.sum(dic[:, :, :])
    # print(dic)
    if debug:
        print("Below is the prediction of dic after normalization")
        np.set_printoptions(formatter={'float': '{:3f}'.format})
        print(dic)
    return dic


def regeneration():
    #p1 = normalization3(HarmonyTable)
    #p2 = normalization3(FluencyTable)
    
    
    # 生成和弦
    '''ChordList = np.zeros((Num), dtype=int)
    pChord = np.zeros((7), dtype=float)
    for i in range(p1.shape[0]):
        pChord[i] = np.sum(p1[i, :, :])
    for i in range(Num):
        c = np.random.choice([1, 2, 3, 4, 5, 6, 7], p=normalization1(pChord).ravel())
        chordList[i] = c'''
    ChordList=[6,3,4,1,2,6,4,3]
    
    TuneList=[]
    for i in range(Num):
        for j in range(8):
            TuneList.append([ChordList[i],-1])
    TuneList[-1]=TuneList[-2]
    TuneLen=len(TuneList)

    # 生成重音
    Prob=StrongHarmony[TuneList[0][0]]
    #print(Prob)
    tunelist=[i for i in range(36)]
    for i in range(36):
        if i<12 or i>23:
            Prob[i]=0
    TuneList[0][1]=np.random.choice(tunelist, p=normalization1(Prob))
    
    for i in range(4,TuneLen,4):
        Prob=StrongHarmony[TuneList[i][0]]
        tunelist=[i for i in range(36)]
        for j in range(36):
            if Note5(j):
                Prob[j]+=0.001
                Prob[j]*=(Adj_Cons(j,TuneList[i-4][1])*Glob_Cons(j))**(1/2)
            else:
                Prob[j]=0
        TuneList[i][1]=np.random.choice(tunelist, p=normalization1(Prob))#H(TuneList[i][0],TuneList[i-2][1])

    for i in range(2,TuneLen-2,4):
        Prob=WeakHarmony[TuneList[i][0]]
        tunelist=[i for i in range(36)]
        for j in range(36):
            if Note5(j):
                Prob[j]+=0.001
                Prob[j]*=(Adj_Cons(j,TuneList[i-2][1])*Adj_Cons(j,TuneList[i+2][1])*Glob_Cons(j))**(1/3)
            else:
                Prob[j]=0
        TuneList[i][1]=np.random.choice(tunelist, p=normalization1(Prob))#H(TuneList[i][0],TuneList[i-2][1])
    Prob=WeakHarmony[TuneList[TuneLen-2][0]]
    tunelist=[i for i in range(36)]
    for i in range(36):
        if Note5(i):
            Prob[i]+=0.001
            Prob[i]*=(Adj_Cons(i,TuneList[TuneLen-4][1])*Glob_Cons(i))**(1/2)
        else:
            Prob[i]=0
    TuneList[TuneLen-2][1]=np.random.choice(tunelist, p=normalization1(Prob))

    # 生成轻音
    for i in range(1,TuneLen-2,2):
        Prob=FluencyTable[TuneList[i+1][1]+12-TuneList[i-1][1]]
        tunelist=[i for i in range(25)]
        #print(Prob)
        for j in range(25):
            if Note5(TuneList[i-1][1]+j):
                Prob[j]+=0.001
                Prob[j]*=(Adj_Cons(j-12,0)*Adj_Cons(TuneList[i-1][1]+j-12,TuneList[i+1][1])*Glob_Cons(TuneList[i-1][1]+j-12))**(1/3)
            else:
                Prob[j]=0
        TuneList[i][1]=TuneList[i-1][1]+np.random.choice(tunelist, p=normalization1(Prob).ravel())-12#F(TuneList[i-1][1],TuneList[i+1][1])
        #print(Prob)
    TuneList[-1]=TuneList[-2]
    return TuneList


def printMusic(TuneList):
    PieceNum = len(TuneList) // 8
    tune = []
    for i in range(PieceNum):
        octave = []
        level = []
        for j in range(8):
            octave.append(TuneList[j+8*i][1] // 12 - 1)
            level.append(Dig_Level(TuneList[j+8*i][1] - (octave[j] + 1) * 12))
        tune.append([Level_Chord(TuneList[i*8][0]),level,octave])
    tune[-1][-1][7]=0
    tune[-1][1][7]=1
    for t in tune:
        for i in t:
            print(i)
    Play(tune)
    
if __name__ == '__main__':
    Calculate()
    music = regeneration()
    printMusic(music)
