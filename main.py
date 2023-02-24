
import copy, random, sys, time

WIDTH = 79 #=sys.argv[1]
HEIGHT = 20 #=sys.argv[2] 

ALIVE = '|'  
DEAD = '-'  
nextCells = {}
aliveCount = 0
stages = 0
isStagnantCount = 0

class Extinction(Exception): pass
class IsolatedSystem(Exception) : pass

for x in range(WIDTH): 
    for y in range(HEIGHT): 
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE 
        else:
            nextCells[(x, y)] = DEAD 

try:
    while True:
        print('\n' * 25) 
        print(f'Current Iteration: Alive = {ALIVE}, Dead = {DEAD} AliveCount: {aliveCount}, Steps to Stagnation: {25 - isStagnantCount}')
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
            
        if isStagnantCount > 25:
            raise(IsolatedSystem)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                left = (x - 1) % WIDTH
                right = (x + 1) % WIDTH
                above = (y - 1) % HEIGHT
                below = (y + 1) % HEIGHT

                numNeighbors = 0
                if cells[(left, above)] == ALIVE:
                    numNeighbors += 1 
                    
                if cells[(x, above)] == ALIVE:
                    numNeighbors += 1 
                    
                if cells[(right, above)] == ALIVE:
                    numNeighbors += 1 
                    
                if cells[(left, y)] == ALIVE:
                    numNeighbors += 1 
                    
                if cells[(left, below)] == ALIVE:
                    numNeighbors += 1 
                    
                if cells[(x, below)] == ALIVE:
                    numNeighbors += 1 
                    
                if cells[(right, below)] == ALIVE:
                    numNeighbors += 1 

                if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                    nextCells[(x, y)] = ALIVE
                    
                elif cells[(x, y)] == DEAD and numNeighbors == 3:
                    nextCells[(x, y)] = ALIVE
                    
                else:
                    nextCells[(x, y)] = DEAD
        stages += 1

        try:
            time.sleep(.5)  
        except KeyboardInterrupt:
            print(f"Conway's Game of Life: Simulation Stages Ran: {stages}")
            sys.exit()  
except IsolatedSystem:
    print(f'Isolated System Became Sustainable After {stages} Simulation Stages')
    sys.exit()  
except Extinction:
    print(f'Colony Has Gone Extinct After {stages} Simulation Stages')
    sys.exit()  