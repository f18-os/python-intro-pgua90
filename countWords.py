#!/usr/bin/env python3

import sys
import os
import subprocess

if len(sys.argv) is not 3:
    print("Correct usage: countWords.py <input text file> <output text file>")
    exit()

inputTxtFile = sys.argv[1]
outputTxtFile = sys.argv[2]

if not os.path.exists("countWords.py"):
    print("wordCount.py does not exist. Exiting")
    exit()

if not os.path.exists(inputTxtFile):
    print("Text file input %s does not exist. Exiting" % inputTxtFile)
    exit()

if not os.path.exists(outputTxtFile):
    print("Text file input %s does not exist. Exiting" % outputTxtFile)
    exit()

subprocess.call(["python3", "./countWords.py", inputTxtFile, outputTxtFile]) #Python file is called and can only run as long as the correct input arguements are given.

#Dictionary, to put all text into.
wordList = {}

#Input file reads line by line; excludes every upper-cased non-alphabetic character.
with open(inputTxtFile, 'r') as file:
    content = file.read()
    line = content.split()
    for word in line:
        foundWord = word.lower().replace(".", "").replace("/", "").replace(",", "") #Each word found discards the non-alphabetic characters to obtain only the alphabetic text.
        if foundWord in wordList: #If the word is found in the list, the number of times the word is found increments.
            wordList[foundWord] +=1 #Counts the number times the word is found.
        else:
            wordList.setdefault(foundWord, 1) #If word is encountered once, by default it is counted only once.
    sortedWords = sorted(wordList) #Words are sorted prior to being implemented into the output text file.

#The output text file is opened and the results from the counted words are inserted within the output text file.
with open(outputTxtFile, 'w') as output:
    for word in sortedWords:
        output.write(word + " " + "%s\n"%wordList[word])
