import sys
import notes

#sys.argv[0] = name of the main file
#sys.argv[1] = function to execute (new, delete, print, update)
#   if new, then take sys.argv[2:], because next args are the text of the new note
#   if delete, then sys.argv[2] = noteID, identifying tag number?
#   if print, then probably no sys.argv[2] or more? just main.py print? or maybe if there is 
#       sys.argv[2] exists after print, then it should be specific ID number, print that note?
#   if update, then sys.argv[2] = noteID, and sys.argv[3:] is the content of the note

num_args = (len(sys.argv) - 1) #number elements excluding name of program

function_name = sys.argv[1]

if function_name == 'new':
    new_note = sys.argv[2:]
    notes.create_sticky(new_note, 'white')
    #TODO create new note if arguments are correct (sanitize?), also need to assign a note ID to it
elif function_name == 'delete':
    if len(sys.argv) == 2:
        notes.delete_all()
    else:
        noteID = sys.argv[2]
        notes.delete_sticky(noteID)
    #TODO retrieve the associated note based on the typed in noteID stored in noteID, and delete it
elif function_name == 'print':
    notes.print_notes()
    #TODO if no more text after print, then print out all notes
    # however, if we give a noteID, print out the note that's associated with it
    # if a note doesn't exist, print out Error: note with that ID does not exist
elif function_name == 'update':
    noteID = sys.argv[2]
    updated_text = sys.argv[3:]
    notes.update_sticky(noteID, updated_text)
else:
    #TODO print out how to use this program, correct syntax for using?
    print('incorrect syntax')


