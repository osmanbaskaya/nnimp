import re
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


d = {'sat':6, 'sun':7,'tue':2,'mon':1,'thu':4,'fri':5,'wed':3,
     'aug': 8, 'nov':11, 'mar':3, 'jun':6, 'jul':7, 'apr':3,
     'may':5, 'dec':12, 'feb':2, 'jan':1, 'sep':9, 'oct':11}


for v, k in d.iteritems():
    d[v] = str(k)

text = open('data/dataforest').readlines()
text = ''.join(text)
with open('dataforest2', 'w') as f:
    f.write(multiple_replace(str(text), d))

