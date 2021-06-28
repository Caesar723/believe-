import random
class people:#people父类
    fail = 0
    win=0
    score=0
    lose=False
    def start(self,give):
        if random.random()<give:
            return True
        else:
            return False
    def check(self,lose):
        None

class pink(people):
    give=1
    team="Pink"

class blue(people):
    give=1
    team ="Blue"
    def check(self,lose):
        if(lose==True):
            self.give=0
        else:
            self.give=1

class yellow(people):
    give=0.5
    team ="Yellow"
class black(people):
    give=0
    team ="Black"
class green(people):
    give=1
    team ="Green"
    mode=0
    record=0
    def check(self,lose):
        if self.mode==0:
            if lose==True:
                self.record+=1
                if self.record==2:
                    self.mode=1
            else:
                self.record=0
        else:
            if (lose == True):
                self.give = 0
            else:
                self.give = 1

def givetype(people):
    typ={
        "<class '__main__.black'>":black(),
        "<class '__main__.yellow'>":yellow(),
        "<class '__main__.green'>":green(),
        "<class '__main__.pink'>":pink(),
        "<class '__main__.blue'>":blue()
    }
    #print(str(type(people)))
    return typ.get(str(type(people)),None)


def stGame(a,b):#进行投币
    if(a.start(a.give)==True and b.start(b.give)==True):
        a.score+=2
        b.score+=2
        a.lose = False
        b.lose = False
    elif a.start(a.give)==True and b.start(b.give)==False:
        a.score-=1
        b.score+=3
        a.lose=True
        b.lose = False
    elif a.start(a.give)==False and b.start(b.give)==True:
        a.score+=3
        b.score-=1
        b.lose=True
        a.lose = False
    else:
        a.lose=True
        b.lose=True
    a.check(a.lose)
    b.check(b.lose)
arr=[]
def team(blu,yello,blac,pin,gree):#把人物放进数组里
    for b in range(0,blu):
        arr.append(blue())
    for y in range(0,yello):
        arr.append(yellow())
    for bl in range(0,blac):
        arr.append(black())
    for p in range(0,pin):
        arr.append(pink())
    for g in range(gree):
        arr.append(green())
#for i in range(0,70):
    #stGame(angela,cheater)
def Csort(array,mark):#进行从小到大排序
    Int=0
    argg=None
    chack=False
    for sco in range(0,len(mark)):
        gg = mark[sco]
        for sc in range(sco+1,len(mark)):

            if gg>mark[sc]:
                gg=mark[sc]
                argg=array[sc]
                Int=sc
                chack=True
        if chack==True:
            mark[Int]=mark[sco]
            mark[sco]=gg
            array[Int]=array[sco]
            array[sco]=argg
            chack=False
def getMark(arr):#放入集合把其score找到
    ma=[]
    for iiii in range(0,len(arr)):
        ma.append(arr[iiii].score)
    return ma
def getTeam(arr):#放入集合把其team找到
    tea=[]
    for iiiii in range(0,len(arr)):
        tea.append(arr[iiiii].team)
    return tea
team(1,0,1,23,0)
for Alltime in range(10):#进行几轮
    #print(getMark(arr))
    for ii in range(0,len(arr)):
        for iii in range(ii+1,len(arr)):
            for time in range(10):  # 每次筛选前比赛几次
                stGame(arr[ii], arr[iii])
            for l in arr:
                l.lose = False
                l.check(l.lose)
    mark=getMark(arr)#开始筛选去掉最低5个变为最高五个
    Csort(arr,mark)
    mark=getMark(arr)
    tea = getTeam(arr)
    get=[]
    for prin in range(0,len(mark)):
        get.append([mark[prin],tea[prin]])
    print(get)
    #print(getTeam(arr))
    print()
    for remove in range(0,5):
        arr[remove]=givetype(arr[-1-remove])
    #mark=getMark(arr)
    for lo in arr:#结束筛选
        lo.score=0
