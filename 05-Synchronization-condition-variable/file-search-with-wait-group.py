import os
import time
from os.path import isdir, join
from threading import Lock, Thread
from WaitGroup import Waitgroup


matches =[]
mutex = Lock()

def file_search(path, file_name, wait_group):

    print(f"Searching in .. {path}")

    child_threads= []

    for file in os.listdir(path):
        full_path = join(path, file)

        if file_name in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()

        if isdir(full_path):

            wait_group.add(1)
            t = Thread(target=file_search , args=(full_path, file_name, wait_group))
            t.start()
            child_threads.append(t)

    wait_group.done()


if __name__ == "__main__":

    wait_group = Waitgroup()
    wait_group.add(1)


    t = Thread(target=file_search, args=(('/media/eldiablo/P4/perse/', '0041_The_Map_Reduce_Architecture--[TutFlix.ORG]--.mp4', wait_group)))
    start = time.time()

    t.start()

    wait_group.wait()

    end = time.time()

    for m in matches:
        print(f"\n\nMatched : {m}")

    print(f"Time taken {end-start}")