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
    def chooseSpec(self,sp):
        self.spec = sp
    def chooseLevel(self,l):
        self.level = 1
    def chooseStats(self):
        emptStat ={"strength":0,"health":0,"defence":0,"magic":0,"intellegence":0,"speed":0}
        maxStat = 10*self.level
        while maxStat > 0:
            print("{}{}{}".format(emptStat["strength"],emptStat["health"],emptStat["defence"]))
            ras = input("Which stat do you wish to increase?\nStrength? Health?\n You have {} points left")
            ras = ras.lower()
            if ras == "strength" or ras == "health" or ras == "defence" or ras == "magic"or ras =="intellegence"or ras =="speed":
                nu = input("Incease stat by how much?")
                if nu.isdigit() == False:
                    while nu.isdigit() == False:
                       nu = input("Not a number please enter again")
                    if nu > maxStat:
                        while nu > maxStat and nu.isdigit == False:
                            nu = input("You don't have enoght points left for that, try entring another number")
                    emptStat[ras]+=nu
                    maxStat = maxStat - nu

    def __str__(self):
        return "{},{},{},".format(self.name,self.spec,self.clas)

def makeChar():
    na = input("Choose a name")
    newchar = char(na)
    cla = input("Choose a class out of these options\nWarrior Cleric Mage Chef Theif Engineer Tamer Ranger or Custom")
    if cla == "custom":
        newchar.chooseClass(cla)
    lev = int(input("What level do you want your character to be?"))
    if lev > 100 or lev<0:
        while lev > 100 or lev<0:
            lev = int(input("Please enter a level between 1 and 100"))
    newchar.chooseLevel(lev)
    newchar.chooseStats()
def viewChar():
    na = input("Enter the characters name")
    open(na,"r")
def compare():
    com1 = input("How do want to choose")
    com2 = input("Who do you want to compare to")
def item():
    eo = input("")


def main():
    ans = input("What would you like to do?\nMake character?  View charcter?  Compare stats?  Equip items? Quit")
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