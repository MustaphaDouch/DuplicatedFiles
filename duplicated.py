import os

# path = 'C:\\Users\\D.Mustapha\\OneDrive\\Desktop\\new_edge'
# path = 'C:\\Users\\D.Mustapha\\OneDrive\\Desktop\\filtest'
path = input('Enter your folder path (C:\...) : ')
f = open(f'{os.getcwd()}\duplicated.txt', 'w', encoding='utf8')
all_files = []
duplicated = {}

for dirpath, dirs, files in os.walk(path):
    # dirpath = dirpath.replace(r'C:\Users\D.Mustapha\OneDrive\Desktop\new_edge',r'Path')
    
    for filename in files: 
        if filename in duplicated.keys():
            duplicated[filename].add(os.path.join(dirpath, filename))
        else:
            duplicated[filename] = {os.path.join(dirpath, filename)}

f.write('-'*20)
f.write(f'\nNumber of duplicated files : {len(duplicated.keys())}\n')
f.write('-'*20 + '\n')
for el in duplicated.keys():
    if len(duplicated[el]) > 1 :
        f.write(f'{el} :\n')
        for i in duplicated[el]:
            f.write(f'    {i}\t: {os.path.getsize(i)/1024} kb\n')
        f.write('\n')

f.close()

os.system(os.getcwd()+'\\duplicated.txt')