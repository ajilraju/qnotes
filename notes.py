#!/usr/bin/env python3


import argparse
import sys
import time

def read_notes():
	# To constantly read from the stdin and send to the files
    # until the # char occurred.  

    line_holder = ""
    done = False	
    print('Put your todo here, (Use # to quit and save from qnotes)')

    while not done:
        read_line = sys.stdin.readline()
        if read_line != '#\n':
            line_holder += read_line
        else:
            done = True
    return line_holder
	                
def write_to_file(notes, title):
	# To open and write the actual notes data to files 
    filename = './taskfile.json'
    
    try:
        file = open(filename, 'a')
        file.write(str({'time': time.time(), 'title': title, 'todo': str(notes)}))
        file.write("\n")
    except IOErro:
        print("Can't write to file")
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser(description='Tool for adding quick todo')
    parser.add_argument('-t','--title',
                                      action='store',
                                      help='set title for the todo\'s')
    parser.add_argument('-l', '--list',                   
                                      action='store_true',
                                      help='view the todo\'s')
    args = parser.parse_args()

    
    if args.title:
        notes_title = args.title
    
    if args.list:
        # Here is showing the stored todo's
	sys.exit(0)
        
    # reading todo from the stdin and once the todo is grabed 
    # the content is write to the file
    notes = read_notes()
    if notes:
	    write_to_file(notes, notes_title)
    else:
	    sys.exit(1)
	
if __name__ == '__main__':
    main()
