import os
from add_entry import Add_Entry
from search_enty import Search


if __name__ == '__main__':


    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def menu(choice):
        if choice == '1':
            add_entry = Add_Entry()
            add_entry.add()
        elif choice == '2':
            search = Search()
            search.search()
        else:
            print("Sorry {} was not an option.".format(choice))


    choice = input('What would you like to do?'
        '\n 1. Add new entry.'
        '\n 2. Search existing entry. \n\n')

    menu(choice)