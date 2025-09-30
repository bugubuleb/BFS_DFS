import os
from collections import deque

#dfs:

def dfs(directory):
    if os.path.isfile(directory):
      if os.path.basename(directory) == 'text.txt':
        print('File found in the directory:', directory)
        included = [x for x in open(directory)]
        sybs = sum(len(x) for x in open(directory))
        if sybs < 50:
          print('File included:', ''.join(included))
        else:
          print(f'File included {sybs} symbols')

    elif os.path.isdir(directory):
        try:
            for item in os.listdir(directory):
                dfs(os.path.join(directory, item))
        except PermissionError:
            pass

#bfs:

def bfs(main_folder):
    queue = deque([main_folder])

    while queue:
        directory = queue.popleft()

        if os.path.isfile(directory):
          if os.path.basename(directory) == 'back.txt':
            print('File found in the directory:', directory)
            included = [x for x in open(directory)]
            sybs = sum(len(x) for x in open(directory))
            if sybs < 50:
              print('File included:', ''.join(included))
            else:
              print(f'File included {sybs} symbols')


        elif os.path.isdir(directory):
            try:
                for x in os.listdir(directory):
                    queue.append(os.path.join(directory, x))

            except PermissionError:
                pass

#bfs and dfs calls:

print('<- bfs ---->')
bfs('folder_1')

print('<- dfs ---->')
dfs('folder_1')
