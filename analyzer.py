import os, sys, json
from config import *
from itertools import combinations
from collections import Counter

class Analyzer:
    def __init__ (self, inputContent):
        self.inputContent = inputContent

    def analyze (self):
        s = self.inputContent
        resultList = []
        sublists = [s[i:i+WINDOW_LEN] for i in range(len(s) - WINDOW_LEN + 1)]
        for l in sublists:
            for length in range(2, WINDOW_LEN + 1):
                head = l[0]
                tmp = combinations(l[1:], length-1)
                tmp2 = [[head] + list(tup) for tup in tmp]
                for sequence in tmp2:
                    if self.timestampConditionFullfilled(sequence):
                        tmp3 = self.extractField(sequence, 'type')
                        resultList.append(tuple(tmp3))
        c = Counter (resultList)
        return [s for s, cnt in c.most_common(RESULT_SIZE)]

    def timestampConditionFullfilled(self, s):
        timestamps = self.extractField(s, 'timestamp')
        if max (timestamps) - min (timestamps) > MAX_TIME_DIFF:
            return False
        #TODO roznica miedzy kazda para
        return True

    def extractField(self, s, field):
        return [event[field] for event in s]

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        jsonContent = f.read()
        print Analyzer(json.loads(jsonContent)).analyze()
