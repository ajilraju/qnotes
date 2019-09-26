#!/usr/bin/env python3

import argparse
import sys

def err_exit(msg):
    sys.stderr.write(msg + '\n')
    sys.exit()

def read_notes():
	# To constantly read from the stdin and send to the files
    # until the # char occurred.  
    done = False	
    print('Put your note here, (Use # to quit and save from notes)')

    while not done:
        read_line = sys.stdin.readline()
        if read_line != '#\n':
            write_to_file(read_line)
        else:
            done = True
	                
def write_to_file(mesg):
	# To open and write the actual notes data to files 
    filename = './notesfiles.txt'
    try:
        file = open(filename, 'w')
        file.write(mesg + '\n')
    except IOError:
        print("Can't write to file")
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser(description='Tool for adding insta notes')
    parser.add_argument('-t','--title',
                                      action='store',
                                      required='True',
                                      help='Set titles for notes.')

    args = parser.parse_args()

    if args.title:
	NOTE_TITLE = args.title
	read_notes()
		
		
if __name__ == '__main__':
   main()
