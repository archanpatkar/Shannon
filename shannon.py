import math
# import ctypes
# import pickle
from pprint import pprint
from fractions import Fraction
from collections import namedtuple, OrderedDict

# Taken from
# https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
def int_to_bytes(number):
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=True)

def int_from_bytes(binary_data):
    return int.from_bytes(binary_data, byteorder='big', signed=True)
# --

def readFile(filename):
    return open(filename,"rb").read()

def writeFile(filename,data):
    return open(filename,"wb").write(data)

def binary(n):
    return bin(n).replace("b","")

def letterFreq(data):
    return {ch: data.count(ch) for ch in data} 

def calcProb(data):
    n = sum(data.values())
    ordered = list(data.items())
    ordered.sort(key=lambda p:p[1])
    d = OrderedDict(ordered)
    for ch in data:
        d[ch] = (data[ch]/n)
    return d

def cumilativeProb(probs):
    ordered = list(probs.items())
    ordered.sort(key=lambda p:p[1], reverse=True)
    probs = OrderedDict(ordered)
    d = OrderedDict()
    k = list(probs.keys())
    d[k[0]] = 0
    last = probs[k[0]]
    for ch in k[1:]:
        d[ch] = probs[ch] + last
        last = probs[ch] + last
    return d

def codeword(cprobs,p2):
    d = OrderedDict()
    for ch in cprobs:
        n = math.ceil(-math.log2(cprobs[ch]))
        d[ch] = binary(math.ceil(p2[ch] * 10000000))[-n:]
    return d

data = readFile("test.txt")
fq = letterFreq(data)
p = calcProb(fq)
cp = cumilativeProb(p)
l = codeword(p,cp)

print("Frequency")
pprint(fq,indent=4)
print("Probability")
pprint(p,indent=4)
print("Cumulative Probability")
pprint(cp,indent=4)
print("Codeword")
pprint(l,indent=4)