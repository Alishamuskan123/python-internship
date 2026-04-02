import datetime
NOTES_FILE='my_notes.txt'
def show_menu():
    """DISPLAY THE MAIN MENU"""
    print('\n'+'='*30)
    print('  NOTES SAVER APP')
    print('='*30)
    print('1. ADD NEW NOTE')
    print('2. VIEW ALL THE NOTES')
    print('3. EXIT')
    print('='*30)
def add_notes():
    """ADD A NEW NOTE TO THE FILE"""
    print('\n---Add new note---')
    note=input('Write your note:').strip()

    if not note:
        print('Cannot save an empty note!')
        return
    
    try:
        #ADD TIMESTAMP(BONUS FEATURE)
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        #OPEN FILE IN APPEND MODE
        with open(NOTES_FILE,'a')as file:
            file.write(f'\n[{timestamp}]\n{note}\n')
            file.write('-'*40+"\n")

        print('NOTE SAVED SUCCESSFULLY!')
    except Exception as e:
        print(f'Error saving note: {e}')
def view_notes():
    """DISPLAY ALL THE SAVED NOTES"""
    print('\n---All saved notes---')

    try:
        #TRY TO OPE AND READ THE FILE
        with open(NOTES_FILE,'r') as file:
            notes=file.read()

            if not notes.strip():
                print('No notes found.Add your first')
                return
            
            print('\n'+'='*40)
            print('YOUR NOTES')
            print('='*40)
            #SPLIT NOTES BY SEPARATOR AND DISPLAY THEM WITH NUMBERS
            note_list=notes.strip().split('-'*40+'\n')

            for i,note in enumerate(note_list,1):
                if note.strip():
                    print(f'\n NOTE#{i}')
                    print(note.strip())
                    print('-'*40)

    except FileNotFoundError:
        print('No notes found!Add your first note!')
    except Exception as e:
        print(f'Error reading notes:{e}')
def main():
    """MAIN PROGRAM LOOP"""
    print('\n WELCOME TO THE NOTES SAVER APPLICATION!')
    while True:
        show_menu()
        try:
            choice=input('\n Choose option(1-3):').strip()
            if choice=="1":
                add_notes()
            elif choice=="2":
                view_notes()
            elif choice=="3":
                print('\n THANKYOU FOR USING NOTES SAVER!')
                print('GOODBYE!\n')
                break
            else:
                print('Invalid choice!Please enter 1,2 or 3.')
        except KeyboardInterrupt:
            print('\n\n Exiting program.Goodbye!')
            break
        except Exception as e:
            print(f'An unexpected error occured:{e}')

#RUN THE PROGRAM
if __name__ =="__main__":
    main()

