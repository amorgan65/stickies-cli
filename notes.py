notes_file = open('notes.txt', 'a+')

line_list = notes_file.readlines()
file_length = len(line_list)

all_notes = []

class Note:
    def __init__(self, content, sticky_color):
        self.sticky_color = sticky_color
        self.content = content

def create_sticky(text, color):
    new_sticky = Note(text, color)
    all_notes.append(new_sticky)
    this_id = get_num_lines('notes.txt')
    notes_file.write(str(this_id) + ': ' + array_to_string(text) + "\n")

def print_square(Note):
    #   _______________
    #  |1              |
    #  |               |
    #  |     NOTE      |
    #  |               |
    #  |_______________|

    print('note id is: ' + Note.tag)
    print('note content is: ' + Note.content)

# Delete sticky note associated with a given ID (shown in top left of note)
def delete_sticky(sticky_id):
    # search data structure of all notes for the one with this ID, 
   # line_list = notes_file.readlines()
    for note in line_list:
        if note[0] == sticky_id:
            print('currently at sticky note that has the given id')
    
def delete_all():
    #TODO delete all sticky notes
    with open('notes.txt') as note_f:
        for line in note_f:
            print('.')
            #TODO delete current line given by line

def print_notes():
    # for each note, check color property, use ANSI tag when printing?
    # https://sparkbyexamples.com/python/print-colored-text-to-the-terminal-in-python/
    with open('notes.txt') as note_f:
        for line in note_f:
            print(line)

def update_sticky(sticky_id, new_text):
    #get the note associated with this ID
    #set current content to null, replace it with 
    print('update sticky note with id ' + sticky_id + ' to have new text: ' + new_text)

#####################
#                   #
# Utility Functions #
#                   #
#####################

def split_line(text):
    noteID = text[0]
    noteText = text[1:] # TODO split up, get rid of the ': '???
    # TODO return list with noteID as first element

# With parameter file_name, create data structure and store file's data into it
def get_file_data(file_name):
    result = {}
    with open(file_name) as note_f:
        for line in note_f:
            separated = split_line(line)
            thisID = separated[0]
            text = separated[1:] #TODO account for the colon in between, separating id and text

    return result

def get_num_lines(file_name):
    result = 0
    with open(file_name) as note_f:
        for line in note_f:
            result += 1

    return result

def array_to_string(array):
    result = ""
    for elem in array:
        result += elem + " "

    return result
