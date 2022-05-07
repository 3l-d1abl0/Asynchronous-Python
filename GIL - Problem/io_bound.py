from threading import Thread, current_thread
from urllib.request import Request, urlopen
import sys
import timeit


def download_file(url, idx=0):
    
    print ('Thread #',idx,' : ', current_thread().name, 'Starts')
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
    webpage = urlopen(req).read()

    with open('sample-video-'+str(idx)+'.mp4', 'wb') as f:
        f.write(webpage)

    print ('Thread #',idx,' : ', current_thread().name, 'Ends\n')


def download_file_using_threads(threads):
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    
    number_of_threads = int(sys.argv[1])
    threads = []

    media_file = "https://jsoncompare.org/LearningContainer/SampleFiles/Video/MP4/Sample-Video-File-For-Testing.mp4"

    #Creeate Threads
    for idx in range(number_of_threads):
        threads.append(Thread(target=download_file, args=(media_file,idx,)))

    #Using Threading
    print(f'Fetching {number_of_threads} files using threads : ')
    print(timeit.timeit("download_file_using_threads(threads)", "from __main__ import download_file_using_threads, threads",
                    number=1))

    #using Serially
    print(f'Fetching {number_of_threads} files serially : ')
    print(timeit.timeit("download_file(media_file,4)", "from __main__ import download_file, media_file", number=number_of_threads))




    '''
    python -m http.server 8000
    /usr/bin/python3 io_bound.py 1
    /usr/bin/python3 io_bound.py 2
    '''