import os
import time
from os.path import isdir, join
from threading import Lock, Thread

matches =[]
mutex = Lock()

def file_search(path, file_name):

    print(f"Searching in .. {path}")

    child_threads= []

    for file in os.listdir(path):
        full_path = join(path, file)

        if file_name in file:
            mutex.acquire()
            matches.append(file_name)
            mutex.release()

        if isdir(full_path):
            t = Thread(target=file_search , args=(full_path, file_name))
            t.start()
            child_threads.append(t)

    for t in child_threads:
        t.join()


if __name__ == "__main__":


    t = Thread(target=file_search, args=(['/media/eldiablo/P4/perse/', '0041_The_Map_Reduce_Architecture--[TutFlix.ORG]--.mp4']))
    start = time.time()

    #file_search('/media/eldiablo/P4/perse/', '0041_The_Map_Reduce_Architecture--[TutFlix.ORG]--.mp4')

    t.start()
    t.join()

    end = time.time()

    for m in matches:
        print(f"Matched : {m}")

    print(f"Time taken {end-start}")