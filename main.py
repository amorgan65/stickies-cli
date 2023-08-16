import sys


#sys.argv[0] = name of the main file
#sys.argv[1] = function to execute (new, delete, print, update)
#   if new, then take sys.argv[2:], because next args are the text of the new note
#   if delete, then sys.argv[2] = noteID, identifying tag number?
#   if print, then probably no sys.argv[2] or more? just main.py print? or maybe if there is 
#       sys.argv[2] exists after print, then it should be specific ID number, print that note?
#   if update, then sys.argv[2] = noteID, and sys.argv[3:] is the content of the note

num_args = (len(sys.argv) - 1)) #number elements excluding name of program










class Note:
    def __init__(self, color, content):
        self.color = color
        self.content = content
        
        #save the sticky notes ID here?

        # save this note in some data structure (hash map??)


def create_sticky(text):
    #create square with |_-?
    #   _______________
    #  |1              |
    #  |               |
    #  |     NOTE      |
    #  |               |
    #  |_______________|

# Delete sticky note associated with a given ID (shown in top left of note)
def delete_sticky(sticky_id):
    # search data structure of all notes for the one with this ID, 


def print_notes():
    # loop through all notes:

    # for each loop, print it on the terminal,
    # for each note, check color property, use ANSI tag when printing?
    # https://sparkbyexamples.com/python/print-colored-text-to-the-terminal-in-python/


def update_sticky(sticky_id, new_text):
    #get the note associated with this ID
    #set current content to null, replace it with 

# TODO put this in another file, note.py, and make this be the connection to backend? or just where command line arguments are parsed
