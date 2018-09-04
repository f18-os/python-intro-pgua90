import sys
import os
import subprocess

if len(sys.argv) is not 3:
    print("Correct usage: count_Words.py <input text file> <output text file>")
    exit()

inputTxtFile = sys.argv[1]
outputTxtFile = sys.argv[2]

if not os.path.exists("count_Words.py"):
    print("wordCount.py does not exist. Exiting")
    exit()

if not os.path.exists(inputTxtFile):
    print("Text file input %s does not exist. Exiting" % inputTxtFile)
    exit()

if not os.path.exists(outputTxtFile):
    print("Text file input %s does not exist. Exiting" % outputTxtFile)
    exit()

subprocess.call(["python3", "./count_Words", inputTxtFile, outputTxtFile])

#Dictionary, to put all text into.
wordList = {}

#Input file reads line by line; excludes every upper-cased non-alphabetic character.
with open(inputTxtFile, 'r') as file:
    content = file.read()
    line = content.split()
    for word in line:
        foundWord = word.lower().replace(".", "").replace("/", "").replace(",", "").replace("-", " ")
        if foundWord in wordList:
            wordList[foundWord] += 1
        else:
            wordList.setdefault(foundWord, 1)

    sortedWords = sorted(wordList)

with open(outputTxtFile, 'w') as output:
    for word in sortedWords:
        output.write(word + " " + "%s\n"%wordList[word])