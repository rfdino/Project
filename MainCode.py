import _json
class char:
    def __init__(self,n):
        self.name = n
        self.spec = ""
        self.clas = ""
        self.back = ""
        self.level = 0
        self.stats = {}
    def chooseBackground(self,b):
        self.back = b
    def getBackground(self):
        return self.back
    def getClass(self):
        return self.clas
    def chooseClass(self,an):
        self.clas = an
    def getName(self):
        return self.name
    def chooseSpec(self,sp):
        self.spec = sp
    def chooseLevel(self,l):
        self.level = l
    def chooseStats(self):
        emptStat ={"strength":0,"health":0,"defence":0,"magic":0,"intellegence":0,"speed":0}
        maxStat = 10*self.level
        while maxStat > 0:
            print(emptStat)
            ras = input("Which stat do you wish to increase?\n You have {} points left".format(maxStat))
            ras = ras.lower()
            nu = int(input("By how much"))
            if nu > maxStat:
                while nu > maxStat:
                        nu = int(input("You don't have enoght points left for that, try entring another number"))
            emptStat[ras]+=nu
            maxStat = maxStat - nu
        self.stats = emptStat

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.name,self.back,self.spec,self.clas,self.level,self.stats)
class inventory:
    def __init__(self,n):
        self.name = n
        self.space = {"0":"empty","1":"empty","2":"empty","3":"empty","4":"empty","5":"empty","6":"empty","7":"empty","8":"empty","9":"empty","10":"empty","11":"empty","12":"empty"}
    def lookup(self,se):
        temp = self.space
        va = 0
        for iv in temp.keys():
            if temp[iv] == se:
                return "{} was found in slot {}".format(se,va)
            va += 1
        return "Couldn't find it"
    def addItem(self,so,it):
        if self.space[so] == "'empty'":
            self.space[so] == it
        else:
            return "Spot has an item already"
    def discard(self,sp):
        if self.space[sp] == "'empty'":
            return "Their is nothing to discard"
        else:
            self.space[sp]= "'empty'"
            return "Item has be discarded"
    def __str__(self):
        return "{},{}".format(self.name,self.space)
    def load(self,n,sp):
        self.name =n
        self.space["0"] = sp[0]
        self.space["1"] = sp[1]
        self.space["2"] = sp[2]
        self.space["3"] = sp[3]
        self.space["4"] = sp[4]
        self.space["5"] = sp[5]
        self.space["6"] = sp[6]
        self.space["7"] = sp[7]
        self.space["8"] = sp[8]
        self.space["9"] = sp[9]
        self.space["10"] = sp[10]
        self.space["11"] = sp[11]
        self.space["12"] = sp[12]
        return self.name

def makeChar():
    na = input("Choose a name\n")
    newchar = char(na)
    cla = input("Choose a class out of these options\nWarrior Cleric Mage Chef Theif Engineer Tamer Ranger or Custom\n")
    newchar.chooseClass(cla)
    sp = input("What species are you?")
    newchar.chooseSpec(sp)
    ba = input("Where are you from?\n")
    newchar.chooseBackground(ba)
    lev = int(input("What level do you want your character to be?"))
    if lev > 100 or lev<0:
        while lev > 100 or lev<0:
            lev = int(input("Please enter a level between 1 and 100"))
    newchar.chooseLevel(lev)
    newchar.chooseStats()
    tempna = newchar.getName()
    tempna += " inv"
    iven = inventory(tempna)
    fi = open(newchar.getName(),"x")
    fi.write(newchar.__str__())
    fi.close()
    iw= open(iven.getName(),"x")
    iw.write(iven.__str__())
    iw.close()
    print(newchar.__str__())
def viewChar():
    na = input("Enter the characters name")
    po = open(na,"r")
    so = po.read()
    out =so.strip().split(",")
    print(out)
    po.close()

def compare():
    com1 = input("Who do want to choose")
    com2 = input("Who do you want to compare to")
    st1 = open(com1,"r")
    ko1 = st1.read()
    jo1 =ko1.strip().split(",")
    st2 = open(com2,"r")
    ko2 = st2.read()
    jo2 = ko2.strip().split(",")
    sta1 = jo1[5]
    strmp = sta1.strip().split(":")
    cmp1 = strmp[1]
    sta2 = jo2[5]
    strmp2 = sta2.strip().split(":")
    cmp2 = strmp2[1]
    cmp1 = int(cmp1)
    cmp2 = int(cmp2)
    if cmp1 > cmp2:
        print(com1+"is stronger")
    elif cmp1 < cmp2:
        print(com2 +"is stronger")
    else:
        print("Same strength")
    he1 = jo1[6]
    sd = he1.strip().split(":")
    tr = sd[1]
    he2 = jo2[6]
    sd2 = he2.strip().split(":")
    tr2 = sd2[1]
    tr = int(tr)
    tr2 = int(tr2)
    if tr > tr2:
        print(com1+" has more health")
    elif tr < tr2:
        print(com2 +" has more health")
    else:
        print("Same health")
    def1 = jo1[7]
    ju = def1.strip().split(":")
    de = ju[1]
    def2 = jo2[7]
    ju2 = def2.strip().split(":")
    de2 = ju2[1]
    de = int(de)
    de2 = int(de2)
    if de > de2:
        print(com1+" has more defence")
    elif de < de2:
        print(com2+" has more defence")
    else:
        print("Same defence")
    mr = jo1[8]
    he = mr.strip().split(":")
    ma = he[1]
    mr2 = jo2[8]
    he2 = mr2.strip().split(":")
    ma2 = he2[1]
    ma = int(ma)
    ma2 = int(ma2)
    if ma > ma2:
        print(com1+" is more magical")
    elif ma < ma2:
        print(com2+" is more magical")
    else:
        print("Same magical abilities")
    ier = jo1[9]
    ite = ier.strip().split(":")
    inel = ite[1]
    ier2 = jo2[9]
    ite2 = ier2.strip().split(":")
    inel2 = ite2[1]
    inel = int(inel)
    inel2 = int(inel2)
    if inel > inel2:
        print(com1+" is more intellegent")
    elif inel < inel2:
        print(com2+" is more intellegent")
    sr = jo1[10]
    ro = sr.strip().split(":")
    spe = ro[1]
    sr2 = jo2[10]
    ro2 = sr2.strip().split(":")
    spe2 = ro2[1]
    spe = spe.strip("}")
    spe2 =spe2.strip("}")
    spe = int(spe)
    spe2 =int(spe2)
    if spe > spe2:
        print(com1+" is faster")
    elif spe < spe2:
        print(com2+" is faster")
    else:
        print("They're the same speed")


def item():
    per = input("Who's inventory do you want to check?")
    per = per+" inv"
    er = open(per,"r")
    po = er.read()
    lo = po.strip().split(",")
    fulInv = [lo[1].strip("{"),lo[2],lo[3],lo[4],lo[5],lo[6],lo[7],lo[8],lo[9],lo[10],lo[11],lo[12],lo[13].strip("}")]
    co = 0
    for iv in fulInv:
        re = iv.split(":")
        op = re[1]
        op.strip("\"")
        fulInv[co] = op
        print(op)
        co +=1
    op = inventory(lo[0])
    op.load(lo[0],fulInv)
    ans = ""
    while ans != "quit":
        print(op.__str__())
        ans = input("What do you want to do?\nAdd item?  discard item?  Search?  Quit?\n")
        ans = ans.lower()
        if ans == "add item":
            th = input("What do you want to add\n")
            sp = input("In which spot?(Enter inventory slot number)\n")
            print(op.addItem(sp,th))
        if ans == "discard item":
            di = input("Which inventory spot do cleared")
            print(op.discard(di))
        if ans == "search":
            se = input("Which item do you want to search for?\n")
            print(op.lookup(se))
        if ans == "quit":
            exit()

def main():
    ans = ""
    while ans != "quit":
        ans = input("What would you like to do?\nMake character?  View charcter?  Compare stats?  Equip items? Quit\n")
        if ans == "make character":
            makeChar()
        elif ans == "view character":
            viewChar()
        elif ans == "compare stats":
            compare()
        elif ans == "equip items":
            item()
        elif ans == "quit":
            exit()

if __name__ == '__main__':
    main()