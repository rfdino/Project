class char:
    def __init__(self,n):
        self.name = n
        self.spec = ""
        self.clas = ""
    def chooseClass(self,an):
        ae = an.lower()
        self.clas = ae
def makeChar():
    na = input("Choose a name")
    newchar = char(na)
    cla = input("Choose a class out of these options\nWarrior Cleric Mage Chef Theif Engineer Tamer Ranger or Custom")


def main():
    ans = input("What would you like to do?\nMake character?  View charcter?  Compare stats?  Equip items?")
    makeChar()

if __name__ == '__main__':
    main()