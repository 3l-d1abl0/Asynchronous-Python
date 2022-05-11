import time
import json
from urllib.request import Request, urlopen


def count_alphabets(url, frequency):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
    webpage = str(urlopen(req).read())

    for alpha in webpage:
        char = alpha.lower()
        if char in frequency:
            frequency[char] +=1


if __name__ == "__main__":

    frequency = dict()
    for char in "abcdefghijklmnopqrstuvwxyz":
        frequency[char]=0

    start = time.time()
    for idx in range(2000, 2030):
        count_alphabets(f"https://www.rfc-editor.org/rfc/rfc{idx}.txt", frequency)


    end = time.time()

    print(json.dumps(frequency, indent=4))
    print("Time Taken ", end-start)