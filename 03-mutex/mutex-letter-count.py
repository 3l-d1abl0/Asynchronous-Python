import time
import json
from urllib.request import Request, urlopen
from threading import Thread, current_thread, Lock


def count_alphabets(url, frequency, mutex):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
    webpage = str(urlopen(req).read())

    mutex.acquire()
    for alpha in webpage:
        char = alpha.lower()
        if char in frequency:
            frequency[char] +=1
    mutex.release()

def download_file_using_threads(threads):
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":

    frequency = dict()
    for char in "abcdefghijklmnopqrstuvwxyz":
        frequency[char]=0


    Threads = []
    mutex = Lock()

    
    for idx in range(2000, 2040):
        Threads.append(Thread(target=count_alphabets, args=(f"https://www.rfc-editor.org/rfc/rfc{idx}.txt", frequency, mutex)))
    
    start = time.time()
    download_file_using_threads(Threads)
    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Time Taken ", end-start)