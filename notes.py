notes_file = open('notes.txt', 'a+')

line_list = notes_file.readlines()
file_length = len(line_list)

all_notes = []

class Note:
    def __init__(self, content, sticky_color):
        self.sticky_color = sticky_color
        self.content = content
             
        #TODO give this note an identifying note ID
        #save the sticky notes ID here?

        # save this note in some data structure (hash map??)


def create_sticky(text, color):
    #create square with |_-?
    #   _______________
    #  |1              |
    #  |               |
    #  |     NOTE      |
    #  |               |
    #  |_______________|
    new_sticky = Note(text, color)
    all_notes.append(new_sticky)
    notes_file.write(str(file_length) + ': ' + str(text))

# Delete sticky note associated with a given ID (shown in top left of note)
def delete_sticky(sticky_id):
    # search data structure of all notes for the one with this ID, 
   # line_list = notes_file.readlines()
    for note in line_list:
        if note[0] == sticky_id:
            print('currently at sticky note that has the given id')
    
   # print('delete note with id ' + sticky_id)

def print_notes():
    # loop through all notes:

    # for each loop, print it on the terminal,
    # for each note, check color property, use ANSI tag when printing?
    # https://sparkbyexamples.com/python/print-colored-text-to-the-terminal-in-python/
    with open('notes.txt') as note_f:
        for line in note_f:
            print(line)


def update_sticky(sticky_id, new_text):
    #get the note associated with this ID
    #set current content to null, replace it with 
    print('update sticky note with id ' + sticky_id + ' to have new text: ' + new_text)

