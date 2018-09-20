#!/usr/bin/env python3

import os, sys, time, re, subprocess, fileInput

def main():
    #When program is executed, a prompt is printed awaited for user input of a command and arguments.
    user_Input = input('$ ') 
    fork(user_Input)
    user_Input2 = input('$ ') 
    pipe(user_Input2)

def fork(user_Input):
    os.write(1, ("About to fork (pid=%d)\n"%pid).encode())

    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n"%rc).encode())
        sys.exit(1)
        
    elif rc == 0:
        
        args = [user_Input]
        os.close(1)
        sys.stdout = open("output.txt", "w")    
        os.set_inheritable(1, True)
        
        for dir in re.split(":", os.environ['PATH']): #Trying each directory in path of where program is located.
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ) #Program is then executed within the child process.
            except FileNotFoundError:
                pass
                print("Command not found.") #If the command is not found the following print statement will be displayed.
            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())l 
            sys.exit(1) #Terminates program with an error.
            
    else:
        os.write(1, ("Parent: pid=%d. Child: pid=%d\n" % (pid, rc)).encode())
        childPidCode = os.wait() #Parent awaits the completion of the child.
        os.write("Parent: Child %d terminated with exit code %d\n" % childPidCode).encode())
        
def pipe(user_Input2):
    pid = os.getpid()
    pr = os.pipe()
    pw = os.pipe()
    
    for f in (pr, pw):
        os.set_inheritable(f, True)
        
    rc = os.fork()
    if rc < 0:
        sys.exit(1)
    elif rc == 0:
        file = sys.stderr
        args = user_Input2
        os.close(1)
        os.dup(pw)
        
        for fd in (pr, pw):
            os.close(fd)
    else:
        file = sys.stderr
        os.close(0)
        os.dup(pr)
        for fd in (pw, pr):
            os.close(fd)
        
 main()   
    
    
    
    
    
