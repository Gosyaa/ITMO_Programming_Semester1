import sys
from datetime import datetime

consolein = sys.stdin
consoleout = sys.stdout

def add(curcat, price):
    curdate = datetime.now().date()
    curdate = str(curdate)
    if cat.get(curcat) == None:
        cat[curcat] = [(price, curdate)]
        allcat.append(curcat)
    else:
        cat[curcat].append((price, curdate))
    if date.get(curdate) == None:
        date[curdate] = [(curcat, price)]
    else:
        date[curdate].append((curcat, price))

def dispall():
    for z in allcat:
        print(z, ':', sep='')
        for q in cat[z]:
            print(q[1], q[0])

def dispcat(curcat):
    if curcat in allcat:
        print(curcat, ':', sep='')
        for q in cat[curcat]: 
            print(q[1], q[0])
    else:
        print("No such category")

def dispdate(curdate):
    if curdate in date.keys():
        for q in date[curdate]:
            print(q[0], q[1])
    else:
        print("No records were made on that date or the format is incorrect")

def sort(key):
    ls = []
    for i in allcat:
        for j in cat[i]:
            ls.append((j[0], i, j[1]))
    ls = sorted(ls)
    if key == '1':
        ls = ls[::-1]
    for i in ls:
        print (i[0], i[1], i[2])

def remove(key):
    global ls, cat, allcat, date
    req = (ls[key][0], ls[key][1], ls[key][2])
    for i in allcat:
        if req[0] == i:
            for j in cat[i]:
                if j[0] == req[1] and j[1] == req[2]:
                    cat[i].remove(j)
            if len(cat[i]) == 0:
                allcat.remove(i)
                cat.pop(i)
            break
    for i in date.keys():
        if i == req[2]:
            for j in date[i]:
                if j[0] == req[0] and j[1] == req[1]:
                    date[i].remove(j)
            if len(date[i]) == 0:
                date.pop(i)
            break

def save(allcat, cat):
    open('save.txt', 'w').close()
    sys.stdout = open('save.txt', 'w')
    ls = []
    for i in allcat:
        for j in cat[i]:
            ls.append((j[0], i, j[1]))
    print(len(ls))
    for i in ls:
        print(i[1], i[0], i[2])
    sys.stdout = consoleout

def load():
    sys.stdin = open('save.txt', 'r')
    try:
        n = int(input())
    except:
        n = 0
    ls = []
    for i in range(n):
        ls.append(())
        a, b, c = input().split()
        b = int(b)
        ls[i] = (a, b, c)
    sys.stdin = consolein
    return ls
    
cat = {}
date = {}
allcat = []
old = load()
for i in old:
    if i[0] in allcat:
        cat[i[0]].append((i[1], i[2]))
    else:
        allcat.append(i[0])
        cat[i[0]] = [(i[1], i[2])]
    if date.get(i[2]) == None:
        date[i[2]] = [(i[0], i[1])]
    else:
        date[i[2]].append((i[0], i[1]))

while True:
    a = input('Enter a command: ')
    a = a.rstrip()
    if a == 'exit':
        c = input('Do you want to save changes? Yes|No\n')
        c = c.rstrip()
        if c == 'Yes':
            save(allcat, cat)
        break

    elif a == 'add':
        c = input('Enter category and price\n').split()
        b = True
        if len(c) != 2:
            print ('wrong input')
            b = False
        try:
            c[1] = int(c[1])
        except:
            print ('wrong input')
            b = False
        if c[1] < 0:
            print ('wrong price')
            b = False
        if b:
            add(c[0], c[1])
            '''curdate = datetime.now().date()
            curdate = str(curdate)
            if cat.get(c[0]) == None:
                cat[c[0]] = [(c[1], curdate)]
                allcat.append(c[0])
            else:
                cat[c[0]].append((c[1], curdate))
            if date.get(curdate) == None:
                date[curdate] = [(c[0], c[1])]
            else:
                date[curdate].append((c[0], c[1]))'''

    elif a == 'display':
        c = input('Type all to display all, type category + category name to display elements from specific category, type date + yyyy-mm-dd date to dislay elements from a specific date\n').split()
        c[0] = c[0].rstrip()
        if c[0] == 'all':
            dispall()
            """for z in allcat:
                print(z, ':', sep='')
                for q in cat[z]:
                    print(q[1], q[0])"""
        elif c[0] == 'category':
            dispcat(c[1])
            """if c[1] in allcat:
                print(c[1], ':', sep='')
                for q in cat[c[1]]: 
                    print(q[1], q[0])
            else:
                print("No such category")"""
        elif c[0] == 'date':
            dispdate(c[1])
            """if c[1] in date.keys():
                for q in date[c[1]]:
                    print(q[0], q[1])
            else:
                print("No records were made on that date or the format is incorrect")"""
        else:
            print('Wrong input')

    elif a == 'sorted':
        c = input('Type 0 to sort from lowet to higest price, type 1 to sort from highest to lowest\n')
        c = c.rstrip()
        if c != '1' and c != '0':
            print("Wrong input")
        else:
            sort(c)
            '''ls = []
            for i in allcat:
                for j in cat[i]:
                    ls.append((j[0], i, j[1]))
            ls = sorted(ls)
            if c == '1':
                ls = ls[::-1]
            for i in ls:
                print (i[0], i[1], i[2])'''

    elif a == 'save':
        save(allcat, cat)
        print('successfully saved')

    elif a == 'delete':
        k = 1
        ls = []
        for z in allcat:
                print(z, ':', sep='')
                for q in cat[z]:
                    print(k, '. ', q[1], ' ', q[0], sep='')
                    ls.append((z, q[0], q[1]))
                    k += 1
        while True:
            g = input('choose a number of a reqired element or print done if there are no more elements to delete\n')
            g = g.rstrip()
            b = True
            if g == 'done':
                break
            try:
                g = int(g)
            except:
                print('wrong input')
                b = False
            if g >= k:
                print('wrong number')
                b = False
            if b:
                remove(g - 1)
                '''req = (ls[g][0], ls[g][1], ls[g][2])
                for i in allcat:
                    if req[0] == i:
                        for j in cat[i]:
                            if j[0] == req[1] and j[1] == req[2]:
                                cat[i].remove(j)
                        if len(cat[i]) == 0:
                            allcat.remove(i)
                for i in date.keys():
                    if i == req[2]:
                        for j in date[i]:
                            if j[0] == req[0] and j[1] == req[1]:
                                date[i].remove(j)
                        if len(date[i]) == 0:
                            date.pop(i)'''
    
    elif a == 'help':
        print('exit - exit from the program\n')
        print('add - add new element\n')
        print('display all elements r some of them\n')
        print('sorted - sort all elements by price\n')
        print('save - save all changes (can also be done with quit before exiting the program\n')
        print('delete - delete some elements\n')
        print('help - list of commands\n')
        
    else:
        print("Sorry, I don't know this command, type help to see all commands available")