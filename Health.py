# Health management system
import os

client_1 = "Ankit"
client_2 = "Harry"
client_3 = "Aditya"


def getdate():
    import datetime

    return datetime.datetime.now()


def lock_food():
    food = ""
    foodname = input("Enter food name: \n")
    food = food + "[" + foodname + "]"
    return food


def lock_Excer():
    Exercise = ""
    excersiename = input("Enter Excersie name: \n")
    Exercise = Exercise + "[" + excersiename + "]"
    return Exercise


def logdetails(clientname, lockdetail):

    print("Logging Details.....")

    with open(clientname, "a") as f:
        f.write("[" + str(getdate()) + "] " + str(lockdetail) + "\n")


def retreive(myclientname):

    if myclientname not in os.listdir():
        return f"File name {myclientname} not exist"
    else:
        with open(myclientname, "r") as f:
            filestr = f.read()
    return filestr


def myfunclock(myclient):
    print(f"Press 1 for food lock and 2 for excersie lock for the client {myclient}")
    _inp = input()
    if _inp == "1":
        f = lock_food()
        myclient = "30. " + myclient + "_food"
        logdetails(myclient, f)
        print("[" + str(getdate()) + "]", f)
    else:
        e = lock_Excer()
        myclient = "30. " + myclient + "_excer"
        logdetails(myclient, e)
        print("[" + str(getdate()) + "]", e)


def myfuncret(myclient):
    print(
        f"Press 1 for food retreive and 2 for excersie retreive for the client {myclient}"
    )
    _inp = input()
    if _inp == "1":
        myclient = "30. " + myclient + "_food"
        stringfile = retreive(myclient)
        print(stringfile)
    else:
        myclient = "30. " + myclient + "_excer"
        lc = retreive(myclient)
        print(lc)


if __name__ == "__main__":

    print("##################")
    print("Welcome to health management system")
    print("Please press 1 for lock the details and 2 for retrieve")
    inp = input()

    if inp == "1":
        print(f"Press 1 to lock the details for {client_1}")
        print(f"Press 2 to lock the details for {client_2}")
        print(f"Press 3 to lock the details for {client_3}")
        lock = input()
        if lock == "1":
            myfunclock(client_1)
        elif lock == "2":
            myfunclock(client_2)
        else:
            myfunclock(client_3)

    if inp == "2":
        print(f"Press 1 to retreive the details for {client_1}")
        print(f"Press 2 to retreive the details for {client_2}")
        print(f"Press 3 to retreive the details for {client_3}")
        retreiveval = input()
        if retreiveval == "1":
            myfuncret(client_1)
        elif retreiveval == "2":
            myfuncret(client_2)
        else:
            myfuncret(client_3)
