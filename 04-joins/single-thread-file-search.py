import os
import time
from os.path import isdir, join

matches =[]

def file_search(path, file_name):

    print(f"Searching in .. {path}")

    for file in os.listdir(path):
        full_path = join(path, file)

        if file_name in file:
            matches.append(file_name)

        if isdir(full_path):
            print("Recu")
            file_search(full_path, file_name)


if __name__ == "__main__":


    start = time.time()

    file_search('/media/eldiablo/P4/perse/', '0041_The_Map_Reduce_Architecture--[TutFlix.ORG]--.mp4')

    end = time.time()

    for m in matches:
        print(f"Matched : {m}")

    print(f"Time taken {end-start}")