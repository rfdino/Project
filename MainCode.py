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
        self.space = {"slot1":"empty","slot2":"empty","slot3":"empty","slot4":"empty","slot5":"empty","slot6":"empty","slot7":"empty","slot8":"empty","slot9":"empty","slot10":"empty","slot11":"empty","slot12":"empty","slot13":"empty"}
    def lookup(self,se):
        temp = self.space
        for iv in temp.keys():
            if temp[iv] == se:
                return "{} was found in ".format(se)
        return "Couldn't find it"
    def addItem(self,so,it):
        if self.space[so] == "empty":
            self.space[so] == it
        else:
            return "Spot has an item already"
    def discard(self,sp):
        if self.space[sp] == "empty":
            return "Their is nothing to discard"
        else:
            self.space[sp]= "empty"
            return "Item has be discarded"


def makeChar():
    na = input("Choose a name\n")
    newchar = char(na)
    cla = input("Choose a class out of these options\nWarrior Cleric Mage Chef Theif Engineer Tamer Ranger or Custom\n")
    newchar.chooseClass(cla)
    ba = input("Where are you from?\n")
    newchar.chooseBackground(ba)
    lev = int(input("What level do you want your character to be?"))
    if lev > 100 or lev<0:
        while lev > 100 or lev<0:
            lev = int(input("Please enter a level between 1 and 100"))
    newchar.chooseLevel(lev)
    newchar.chooseStats()
    fi = open(newchar.getName(),"x")
    fi.write(newchar.__str__())
    fi.close()
    print(newchar.__str__())
def viewChar():
    na = input("Enter the characters name")
    open(na,"r")
def compare():
    com1 = input("How do want to choose")
    com2 = input("Who do you want to compare to")
def item():
    eo = input("")


def main():
    ans = input("What would you like to do?\nMake character?  View charcter?  Compare stats?  Equip items? Quit\n")
    if ans == "make character":
        makeChar()
    elif ans == "view character":
        viewChar()
    elif ans == "compare stats":
        compare()
    elif ans == "equip":
        item()
    elif ans == "quit":
        exit()

if __name__ == '__main__':
    main()