import re
import json
from IPython.display import clear_output
x = '='*53
y = '='*8
z = '^'*53
run = True
print(f'|{z}|\n|{x}|\n|{y} Welcome to School Management System {y}|\n|{x}|\n|{z}|\n\n')
try:
    li = open('me.json','r')
    listStd = json.load(li)
except:
    listStd = {}
    with open('me.json','w') as fp:
        json.dump(listStd, fp)
    li = open('me.json')
    listStd = json.load(li)
while run:
    clear_output()
    x = '='*53
    y = '='*8
    z = '^'*53
    run = True
    print(f'|{z}|\n|{x}|\n|{y} Welcome to School Management System {y}|\n|{x}|\n|{z}|\n\n')
    
    
    
    print('Option 1: View all students\nOption 2: Register a new student\nOption 3: Remove a student\nOption 4: Search for a student')
    ing = input('\nWhat do you want to do? ')
    
              
    if ing == '1':
        print(listStd)
        
            
            
    elif ing =='2':
        ad = input('Name of student you want to add: ')
        try:
            ag = int(input('Age of student: '))
        except:
            print('Enter a number!')
        listStd[ad] = ag
        with open("me.json", "w") as fp:
            json.dump(listStd,fp) 
        print(listStd)
        
            
    elif ing == '3':
        rm = input('Name of student you want to remove: ')
        if rm in listStd:
            listStd.pop(rm)
            with open("me.json", "w") as fp:
                json.dump(listStd,fp) 
            print(f'\n{listStd}')
        elif rm not in listStd:
            print(f'There is no record of a student called {rm}\nDo you wish to register them instead?(Press 2)')
        
            
    elif ing == '4':
        srch = input('Do you know the initial letters of the name(Any number of them)? Type it here: ')
        print('\n')
        srch = srch.capitalize()
        print('Here are some matches: ')
        c = []
        for item in listStd:
            found = re.findall(srch, item)
            if len(found) > 0:
                print(item)
                c.append(found[0])
        if len(c) == 0:
            print('No matches found!')
            
                
            
    end = input('Do you want to exit? y/n ')
    if end == 'n':
        pass
    elif end == 'y':
        run = False            
            
else:
    c = '<'*16
    d = '>'*16
    print(f'\n{c}Goodbye{d}\n')
    
    
