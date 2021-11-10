from threading import Thread, current_thread
import urllib.request
import sys
import timeit


def download_file(url):
    urllib.request.urlretrieve(url, f'{current_thread().name}')


def download_file_using_threads(threads):
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    
    number_of_threads = int(sys.argv[1])
    threads = []

    media_file = "http://localhost:8000/Mastering%20Chaos%20-%20A%20Netflix%20Guide%20to%20Microservices.mp4"
    
    for _ in range(number_of_threads):
        threads.append(Thread(target=download_file, args=(media_file,)))
        
        
    print(timeit.timeit("download_file_using_threads(threads)", "from __main__ import download_file_using_threads, threads",
                    number=1))

    '''
    python -m http.server 8000
    /usr/bin/python3 io_bound.py 1
    /usr/bin/python3 io_bound.py 2
    '''