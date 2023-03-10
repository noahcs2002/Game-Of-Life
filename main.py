
import copy, random, sys, time
from settings import *
from exceptions import *

nextCells = {}

def populateBoard():
    for x in range(WIDTH): 
        for y in range(HEIGHT): 
            if random.randint(0, 1) == 0:
                nextCells[(x, y)] = ALIVE 
            else:
                nextCells[(x, y)] = DEAD 

populateBoard()

try:
    while True:
        print('\n' * 25) 
        print(f'Current Iteration: Alive = {ALIVE}, Dead = {DEAD}, AliveCount: {aliveCount}, Steps to Stagnation: {stagCount - isStagnantCount}')
        cells = copy.deepcopy(nextCells)
        aliveOldCount = aliveCount
        aliveCount = 0
        
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if cells[(x,y)] == ALIVE:
                    aliveCount += 1
                    
                print(cells[(x, y)], end = '') 
            print()  
        print('Press Ctrl-C to quit.')
        print(f'Sim Count: {stages}')
        
        if aliveCount == 0:
            raise(Extinction)
        if aliveCount == aliveOldCount:
            isStagnantCount += 1
        else:
            isStagnantCount = 0
            
        if isStagnantCount > stagCount:
            raise(IsolatedSystem)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                left = (x - 1) % WIDTH
                right = (x + 1) % WIDTH
                above = (y - 1) % HEIGHT
                below = (y + 1) % HEIGHT

                neighborCount = 0
                if cells[(left, above)] == ALIVE:
                    neighborCount += 1 
                    
                if cells[(x, above)] == ALIVE:
                    neighborCount += 1 
                    
                if cells[(right, above)] == ALIVE:
                    neighborCount += 1 
                    
                if cells[(left, y)] == ALIVE:
                    neighborCount += 1 
                    
                if cells[(left, below)] == ALIVE:
                    neighborCount += 1 
                    
                if cells[(x, below)] == ALIVE:
                    neighborCount += 1 
                    
                if cells[(right, below)] == ALIVE:
                    neighborCount += 1 

                if cells[(x, y)] == ALIVE and (neighborCount == 2 or neighborCount == 3):
                    nextCells[(x, y)] = ALIVE
                    
                elif cells[(x, y)] == DEAD and neighborCount == 3:
                    nextCells[(x, y)] = ALIVE
                    
                else:
                    nextCells[(x, y)] = DEAD
        stages += 1

        try:
            time.sleep(.5)  
        except KeyboardInterrupt:
            print(f"Simulation Stopped Prematurely: Simulation Stages Ran: {stages}")
            sys.exit()  
except IsolatedSystem:
    print(f'Isolated System(s) of Total Size {aliveCount} Became Sustainable After {stages} Simulation Stages')
    saveResult = input('Save simulation result to file y/[n]?\n')
    if saveResult.lower() == 'y':
        file = open(path, 'w+')
        file.write(f'Current Iteration: Alive = {ALIVE}, Dead = {DEAD}, AliveCount: {aliveCount}, Steps to Stagnation: {stagCount - isStagnantCount}')
        file.write(f'\n')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                file.write(cells[(x,y)])
            file.write('\n')
        file.write(f'Isolated System(s) of Total Size {aliveCount} Became Sustainable After {stages} Simulation Stages')
        
    
except Extinction:
    print(f'All Colonies Have Gone Extinct After {stages} Simulation Stages')
    saveResult = input('Save simulation result to file y/[n]?\n')
    if saveResult.lower() == 'y':
        file = open(path, 'w+')
        file.write(f'Current Iteration: Alive = {ALIVE}, Dead = {DEAD}, AliveCount: {aliveCount}, Steps to Stagnation: {stagCount - isStagnantCount}')
        file.write(f'\n')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                file.write(cells[(x,y)])
            file.write('\n')
        file.write(f'All Colonies Have Gone Extinct After {stages} Simulation Stages')

        
