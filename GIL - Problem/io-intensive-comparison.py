import time
import urllib.request
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen

urls = ['http://www.discovertunisia.com',
        'http://whc.unesco.org/en/list/38',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8'
        'http://www.tourismtunisia.com/10-adventurous-things-to-do-in-tunisia/',
        'http://wowtravel.me/top-10-things-to-do-in-tunisia/',
        'http://en.wikipedia.org/wiki/Tataouine',
        'http://en.wikipedia.org/wiki/Carthage',
        'http://en.wikipedia.org/wiki/Hannibal',
        'http://www.discovertunisia.com',
        'http://whc.unesco.org/en/list/38',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8'
        'http://www.tourismtunisia.com/10-adventurous-things-to-do-in-tunisia/',
        'http://wowtravel.me/top-10-things-to-do-in-tunisia/',
        'http://en.wikipedia.org/wiki/Tataouine',
        'http://en.wikipedia.org/wiki/Carthage',
        'http://en.wikipedia.org/wiki/Hannibal'
        ]


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def fetch_url(x):
    print ('Thread #',x,' : ', threading.current_thread().name, 'Starts')
    
    try:
        req = Request(urls[x], headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
        webpage = urlopen(urls[x]).read()

    except Exception as ex:
        print(ex, ' : ' ,urls[x])

    print ('Thread #',x,' : ', threading.current_thread().name, 'Ends \n')


if __name__ == "__main__":
    
    number_of_threads = len(urls)

    #Serially
    marker = time.time()
    for idx in range(number_of_threads):
        fetch_url(idx)
        
    print("Time Taken : ", time.time() - marker,"\n\n\n")

    #Multithreading
    #for n_threads in [4, 8, 16]:
    marker = time.time()
    multithreading(fetch_url, range(number_of_threads), number_of_threads)
    
    print("Multithreading {} spent".format(number_of_threads), time.time() - marker)
