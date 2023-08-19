import sys
import notes

num_args = (len(sys.argv) - 1) #number elements excluding name of program

function_name = sys.argv[1]

if function_name == 'new':
    new_note = sys.argv[2:]
    #TODO take in color if provided to allow different sticky note colors?
    notes.create_sticky(new_note, 'white')
    #TODO create new note if arguments are correct (sanitize?), also need to assign a note ID to it
elif function_name == 'delete':
    if len(sys.argv) == 2:
        notes.delete_all()
    else:
        noteID = sys.argv[2]
        notes.delete_sticky(noteID)
elif function_name == 'print':
    if len(sys.argv) == 2:
        notes.print_notes()
    #TODO create function in notes.py to print a single note, by a given ID?

elif function_name == 'update':
    if len(sys.argv) < 4:
        print('Not enough arguments provided')
    else:
        noteID = sys.argv[2]
        updated_text = sys.argv[3:]
        notes.update_sticky(noteID, updated_text)
else:
    #TODO print out how to use this program, correct syntax for using?
    print('incorrect syntax')

