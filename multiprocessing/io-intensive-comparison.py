from multiprocessing import Process, current_process
from concurrent.futures import ProcessPoolExecutor
from urllib.request import Request, urlopen
import sys
import time

media_file = "https://jsoncompare.org/LearningContainer/SampleFiles/Video/MP4/Sample-Video-File-For-Testing.mp4"

def download_file(media_file, idx):
    
    print ('Process #',idx,' : ', current_process().name, 'Starts')
    
    req = Request(media_file, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
    video = urlopen(req).read()

    with open('sample-video-'+str(idx)+'.mp4', 'wb') as f:
        f.write(video)

    print ('Process #',idx,' : ', current_process().name, 'Ends\n')


def download_file_using_processes(func, media_file, args, workers):
    
    #(max_workers)
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, [media_file]*len(args), args)    #loop arg times
    #return list(res)

if __name__ == "__main__":
    
    number_of_processes = int(sys.argv[1])



    #Serially
    
    marker = time.time()
    for idx in range(number_of_processes):
        download_file(media_file, idx)

    print(f'Time taken Serially ={time.time()-marker} ')
    

    #Multithreading
    marker = time.time()
    download_file_using_processes(download_file, media_file, range(number_of_processes), number_of_processes)
    
    print("Multithreading {} spent".format(number_of_processes), time.time() - marker)



    '''
    python -m http.server 8000
    /usr/bin/python3 io_bound.py 1
    /usr/bin/python3 io_bound.py 2
    '''