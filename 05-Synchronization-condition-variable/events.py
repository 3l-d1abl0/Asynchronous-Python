import threading

event = threading.Event()


def myFunction():

    print("Waiting for event to trigger ...")
    event.wait()
    print("Trigerred !")


if __name__ == "__main__":

    t = threading.Thread(target=myFunction)
    t.start()

    x = "val"

    while x != "y":
        x  = input("Trigger the Event (y/n) \n")
        if x == "y":
            event.set()