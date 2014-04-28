import os, sys, json

class Analyzer:
    def __init__ (self, inputRawContent):
        self.inputContent = json.loads(inputRawContent)

    def analyze (self):
        return self.inputContent

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        jsonContent = f.read()
        print Analyzer(jsonContent).analyze()
