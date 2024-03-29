import os
import math

def megaCalc(size):
    if size < 1024:
        return f'{size} byte'
    elif size > 1024:
        size = size/1024
        if size > 1024:
            size = (size/1024)
            if size > 1024:
                size = size/1024
                return f'{math.floor(size)} Gb'
            return f'{math.floor(size)} Mb'            
        return f'{math.floor(size)} kb'
    
    

def countCalc(dup):
    for j in dup:
        count = 0
        for k in dup:
            if k == j:
                count += 1
        return count, j




print('*'*20, 'WELCOME TO DUPLICATED APP', '*'*20)
print('1    all duplicated files (by name)')
print('2    duplicated files (name & size)')
print('3    duplicated files sorted by size (prefered)')

choice = ''
path = ''


while path == '':
    path = input('Enter your folder path (C:\...) : ')
while choice == '':
    choice = input('Enter your choice : ')
f = open(f'{os.getcwd()}\duplicated.txt', 'w', encoding='utf8')
all_files = []
duplicated = {}
i = 0
for dirpath, dirs, files in os.walk(path):
    # p = dirpath
    # dirpath = dirpath.replace(r'C:\Users\D.Mustapha\OneDrive\Desktop\new_edge',r'Path')
    
    for filename in files: 
        if filename in duplicated.keys():
            duplicated[filename].append([os.path.join(dirpath, filename), os.path.getsize(os.path.join(dirpath, filename))])
        else:
            duplicated[filename] = [[os.path.join(dirpath, filename), os.path.getsize(os.path.join(dirpath, filename))]]


f.write('-'*20)
# f.write(f'\nNumber of duplicated files : {len(duplicated.keys())}\n')
f.write('\nDUPLICATED FILES:\t\t\n')
f.write('-'*20 + '\n')
dup = []
dupSizes = []
totSize = []
for el in duplicated.keys():
    dup = []
    if len(duplicated[el]) > 1 :
        for a in duplicated[el]:
            dup.append(a[1])

        ''' choice number 1'''
        if choice == '1':
                f.write(f'{el} :\n')
                for i in duplicated[el]:
                    f.write(f'    {i[0]}\t: {megaCalc(i[1])} \n')
                f.write('\n')

    ''' choice number 2'''
    if choice == '2':
        if len(dup) != len(set(dup)):
            count, j = countCalc(dup)
            if count > 1:
                for p in duplicated[el]:
                    w = 0
                    for t in p:
                        w+=p[1]
                f.write(f'{el} (size : {megaCalc(w)}):\n')
                for i in duplicated[el]:    
                    if i[1] == j:
                        f.write(f'    {i[0]}\t: {megaCalc(i[1])} \n')

                f.write('\n')
    
    if choice == '3':
        
        if len(dup) != len(set(dup)):
            count, j = countCalc(dup)
            if count > 1:
                for p in duplicated[el]:
                    w = 0
                    for t in p:
                        w+=p[1]
                # f.write(f'{el} (size : {megaCalc(w)}):\n')
                for i in duplicated[el]:    
                    if i[1] == j:
                        # f.write(f'    {i[0]}\t: {i[1]} kb\n')
                        dupSizes.append([w, el,[i[0], i[1]]])
                        totSize.append(w)
                        
if choice == '3':
    z = sorted(dupSizes, key=lambda x: x[0])
    z.reverse()
    # first = z[0][1]D:\.Master\PFE\Rapport_finale    
    # last = z[0][1]
    # print(z)
    last = ''
    # f.write(f'\n{z[0][1]} (size : {megaCalc(z[0][0])}):\n')
    for i in z:
        first = i[1]
        if first != last :
            f.write(f'\n{i[1]} (size : {megaCalc(i[0])}):\n')
        
        f.write(f'    {i[2][0]}\t: {megaCalc(i[2][1])} \n')
            
        last = i[1]
        
f.close()

os.system(os.getcwd()+'\\duplicated.txt')


input('Press Enter to exit')
