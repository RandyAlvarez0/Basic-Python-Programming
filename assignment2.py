import socket


class Assignment2:
    year = 0
    currentYear = 0

    # Task 1 (Constructor)
    def __init__(self, year):
        self.year = year

    # Task 2 (Age)
    def tellAge(self, currentYear):
        self.currentYear = currentYear
        return print("Your age is " + str(currentYear - self.year))

    # Task 3 (List)
    def listAnniversaries(self):
        anniList = []
        diff = int(self.currentYear - self.year)
        rep = int(diff / 10)
        for x in range(rep):
            anniList.append((x + 1) * 10)

        return anniList

    # Task 4 (String Manipulation)
    def modifyYear(self, n):
        list1 = []
        list2 = []
        textRep = str(self.year)
        textRepMulti = str(n * self.year)

        for x in range(n):
            list1.append(textRep[0])
            list1.append(textRep[1])

        for x in range(0, len(textRepMulti)):
            count = x + 1
            if count % 2:
                list2.append(textRepMulti[x])

        strings1 = [str(integer) for integer in list1]
        a_string1 = "".join(strings1)

        strings2 = [str(integer) for integer in list2]
        a_string2 = "".join(strings2)

        a_string1 += a_string2
        return a_string1

    # Task 5 (Loop and Conditional statements)
    @staticmethod
    def checkGoodString(string):
        truthState = False
        counter = 0
        if len(string) >= 9 and string[0].islower() == True:
            for x in range(len(string)):

                if string[x].isdigit():
                    counter += 1

            if counter == 1:
                truthState = True

        return truthState

    # Task 6 (Socket)
    @staticmethod
    def connectTcp(host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()
            return True
        except:
            return False


a = Assignment2(2000)
a.tellAge(2030)
ret = a.listAnniversaries()
print(ret)

a = Assignment2(1991)
a.tellAge(2030)
ret = a.listAnniversaries()
print(ret)

a = Assignment2(1782)
ret = a.modifyYear(3)
print(ret)

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
