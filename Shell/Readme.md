Shell Lab


Project Description

The assignment consisted of the student to become familiar with Shells and how to create Shell scripts with Python. The lab assigned 

Testing Description
Using the professor's source code as reference, I decided to use the part concerning the input of the text files, both input and output files. With this, what is used as a Dictionary, with the variable name "wordList", which would keep the list of words obtained from teh text file.
Used as well from the reference code, I had the file read, in the format of being read line by line and split between whitespaces. For each text found, text that excluded upper-cased text and removed non-alphabetic characters from the text found. An if-statement was created so as to count the number of occurrences of that text were to be found within the file, with a default number of 1, if occurrence of the text was only once. The list of words were then sorted and another file was created in order to store the newly added list of words, each with their respective number of occurrences.


This assignment was prepared in a manner consistent with the instructor's requirements. All significant collaboration or guidance from external sources is clearly documented.
Resources used:
* Used Dr. Freudenthal's source codes - (Used the Professor's source codes and used certain parts into my code, since they provided a better reference towards how the commands were used in Python. I implemented the use of the fork, execute, redirection and piping, whilst with the use of this, I was able to add the content that I needed in order to perform the tasks that were asked according to the assignment. I also used his testShell in order to test my own Python script to keep in awareness as to which mistakes I was making in my code.
    
* Used the following sites:
    *https://www.poftut.com/execute-shell-command-python/ - (Page was used in order to better understand the how to implement the parameters when using the Python Subprocess)
    *www.cs.uleth.ca/~holzmann/C/system/pipeforkexec.html - (Page was used in order to grasp a better understanding of the commands, but mostly for obtaining a better visual on how to implement the use of piping)
    *https://www.geeksforgeeks.org/dup-dup2-linux-system-call/ - (I referenced from site, in order to know more about the use of the dup() and dup2() calls and how they're used concerning the file descriptors, which this provided me with a better visual)
    *www.sarathlakshman.com/2012/09/24/implementation-overview-of-redirection-and-pipe-operators-in-shell - (Used site to have a simpler understanding for each of the commands in shell; used the visuals as references on how to go about using redirection and piping.
