import shutil
from pathlib import Path

firstfile = Path('1.txt')
secondfile = Path('2.txt')

newfile = '3.txt'

with open(newfile, "wb") as wfd:
    for f in [firstfile, secondfile]:
        with open(f, "rb") as fd:
            shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)



a_file = open("1.txt", "r",encoding='utf-8')

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()




a_file2 = open("2.txt", "r",encoding='utf-8')
list_of_lists2 = []
for line2 in a_file2:
  stripped_line2 = line2.strip()
  line_list2 = stripped_line2.split()
  list_of_lists2.append(line_list2)

a_file2.close()



if len(list_of_lists) > len(list_of_lists2):
    print('1.txt')
    print(len(list_of_lists))

    for x in list_of_lists:
        print(" " . join(x))
    print('2.txt')
    print(len(list_of_lists2))
    for y in list_of_lists2:
        print(" " . join(y))
else:
    print('2.txt')
    print(len(list_of_lists2))
    for q in list_of_lists2:
        print(" " . join(q))
    print('1.txt')
    print(len(list_of_lists))
    for w in list_of_lists:
        print(" " . join(w))

