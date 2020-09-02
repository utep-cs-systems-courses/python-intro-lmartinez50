# Copyright (c) 2020 Lorenzo Martinez
#
# This program takes as input the name of an input file and output file
# keeps track of the total the number of times each word occurs in the text file
# excluding white space and punctuation is case-insensitive
# print out to the output file (overwriting if it exists) the list of words
# sorted in descending order with their respective totals separated by a space, one word per line
#
# Author Lorenzo Martinez
# Version 1.0
# Creation Date: 08/30/2020
# Due date: 09/02/2020
# Lab 1
# CS 4375 Theory of Operating Systems
# Instructor PhD Eric Freudenthal
# Rev. 1 08/30/2020 Initial approach
# Rev. 2 08/31/2020

import re       # regular expression tools
import sys      # command line arguments

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCountTest.py <input text file> <output text file>")
    exit()

# List of arguments
inputFName = sys.argv[1]
outputFName = sys.argv[2]

#Dictionary to store the words
words = {}

with open(inputFName, 'r') as thisFile:
    for line in thisFile:
        line = line.strip()                             # remove newline characters
        for word in re.split("[\"'\s\t.,-;:?!]", line): # split at spaces, punctuation, tab
            if word.lower() == "":
                continue
            if word.lower() in words:                   # if word is already in words dict, add 1 to count for that
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1

# Write to output file
file = open(outputFName, "w+")

# Close the file
file.close() # close the output file when done

