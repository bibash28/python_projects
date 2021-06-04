import pygame

pygame.init()

size = width,height = 1400, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Missionaries and Cannibals Tree")
font = pygame.font.SysFont('Comic Sans MS', 18)

red = (0,0,255)
blue = (0,208,208)

clock = pygame.time.Clock()

class LeftBank:
    def __init__(self):
        self.mis = 3
        self.can = 3

class RightBank:
    def __init__(self):
        self.mis = 0
        self.can = 0

class Boat:
    def __init__(self):
        self.inLeft = True
        self.mis = 0
        self.can = 0

class State:
    def __init__(self,m_state,c_state,b_state):
        self.index = -1
        self.children = []
        self.m_state = m_state
        self.c_state = c_state
        self.boat_state = b_state
        self.isVisited = False
        self.tot_state = [self.m_state,self.c_state, self.boat_state]

    def setPos(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos


initial_state,final_state = [[3,3,True],[0,0,True]],[[0,0,False],[3,3,False]]

queue = [initial_state]

data = []

state = State(initial_state[0][0], initial_state[0][1], initial_state[0][2])
state.index = 0

leftBank = LeftBank()
rightBank = RightBank()
boat = Boat()

root_state = state
parent_state = state

state_queue = [parent_state]
nodes = [parent_state]

def set_original_value(leftBank,rightBank,boat,m,c):
    boat.inLeft = not boat.inLeft
    if boat.inLeft == True:
        leftBank.mis += m
        leftBank.can += c
        rightBank.mis -= m
        rightBank.can -= c
    else:
        rightBank.mis += m
        rightBank.can += c
        leftBank.mis -= m
        leftBank.can -= c

while True:
    current_state = queue.pop(0)
    current_parent_state = state_queue.pop(0)

    if (current_state[0][1] > current_state[0][0] and current_state[0][0] != 0) or (current_state[1][1] > current_state[1][0] and current_state[1][0] != 0):
        #print("Invalid Condition")
        continue
    if (current_state == final_state):
        done = True
        break

    leftBank.mis,leftBank.can = current_state[0][0],current_state[0][1]
    rightBank.mis, rightBank.can = current_state[1][0],current_state[1][1]
    boat.inLeft = current_state[0][2]

    mis_travel,can_travel = -1 ,-1

    #   Possible Number of missionaries or cannibals to travel
    if (boat.inLeft == True):
        mis_travel = (2 if leftBank.mis >2 else leftBank.mis)
        can_travel = (2 if leftBank.can >2 else leftBank.can)
    else:
        mis_travel = (2 if rightBank.mis >2 else rightBank.mis)
        can_travel = (2 if rightBank.can >2 else rightBank.can)

    for m in range(mis_travel + 1):
        for c in range(can_travel + 1):
            if (m+c >2 or m+c == 0):
                continue
            boat.mis = m
            boat.can = c

            if boat.inLeft == True:      # boat is in the left bank
                leftBank.mis -= m
                leftBank.can -= c
                rightBank.mis += m
                rightBank.can += c
            else:                        # boat is in the right bank
                leftBank.mis += m
                leftBank.can += c
                rightBank.mis -= m
                rightBank.can -= c
            boat.inLeft = not(boat.inLeft)
            this_state = [[leftBank.mis, leftBank.can, boat.inLeft],[rightBank.mis, rightBank.can, boat.inLeft]]

            if (this_state not in data):
                if (this_state not in queue):
                    queue.append(this_state)

                    temp_state = State(this_state[0][0],this_state[0][1],this_state[0][2])
                    temp_state.index = current_parent_state.index + 1
                    current_parent_state.children.append(temp_state)
                    state_queue.append(temp_state)
                    nodes.append(temp_state)
            set_original_value(leftBank,rightBank,boat,m,c)
    data.append(current_state)

#   To draw each node and its children in the screen
def draw(node):
    if len(node.children) > 0:
        for i in range(len(node.children)):
            x_pos, y_pos = node.x_pos + 90, (node.y_pos + i * 75 if node.y_pos + i * 75 < height else node.y_pos - i * 75)
            node.children[i].setPos(x_pos,y_pos)
            pygame.draw.line(screen,blue,(node.x_pos,node.y_pos),(x_pos,y_pos),1)
            pygame.draw.circle(screen,red,(x_pos,y_pos),5)
            textSurface = font.render(str(node.children[i].m_state) + "," + str(node.children[i].c_state) + "," + str(node.children[i].boat_state),False,(0,1,0))
            screen.blit(textSurface,(x_pos-textSurface.get_width()/2 , y_pos + textSurface.get_height()/2))
            draw(node.children[i])
         
while True:
    screen.fill((240,248,255))
    

    #   Draw root node in the screen
    nodes[0].setPos(75,20)
    pygame.draw.circle(screen,red,(nodes[0].x_pos,nodes[0].y_pos),5)
    textSurface = font.render(str(nodes[0].m_state) + "," + str(nodes[0].c_state) + "," + str(nodes[0].boat_state),False,(0,1,0))
    screen.blit(textSurface,(nodes[0].x_pos-textSurface.get_width()/2 , nodes[0].y_pos + textSurface.get_height()/2))
    draw(nodes[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick(50)
    pygame.display.update()


