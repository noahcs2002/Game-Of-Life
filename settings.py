import os

WIDTH = 79 #=sys.argv[1]
HEIGHT = 20 #=sys.argv[2] 
login = os.getlogin()
path = f'C:\\Users\\{login}\\Desktop\\GOL.txt'

ALIVE = '|'  
DEAD = '-'  
aliveCount = 0
stages = 0
isStagnantCount = 0
stagCount = 5