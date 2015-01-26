"""
Lecture 7 - OOP (Robot survival / treasure hunt simulator)

Changelog:
ver 2 = bugfix (width and height typo in print_state())
ver 3 = added Agent.compass() function to get current heading
ver 4 = added 90-degree turns and endurance counter (you can do turn(-2) or turn(2) but lose endurance
        if you have no endurance, then you do a regular 45 degree turn, use this to get out of a certain crash)


@author gert
"""
import hashlib
import time
import random

class RegistrationException(Exception):
    pass
class RobotWallCrashException(Exception):
    pass
class RobotCollisionException(Exception):
    pass
class RobotFoundTreasureException(Exception):
    pass
class RobotObjectCrashException(Exception):
    pass


class World:
    width = 0
    height = 0
    robots = [] # Robot state = [x, y, direction, turn, [turn history], endurance]
    time = 0
    sleep_time = 0
    items = [] # Items in the world= [x, y, type], type = 1 : treasure, type = 2 : obstacle
    
    def __init__(self, width, height, sleep_time = 1, treasure = None, obstacles = None, reliability = 0.9, endurance = 1000):
        self.height = height
        self.width = width
        self.time = 0
        self.sleep_time = sleep_time
        self.reliability = reliability
        self.endurance = endurance
        random.seed()
        if treasure == None:
            self.items.append([random.randint(0, width-1), random.randint(0, height-1), 1])
        else:
            self.items.append([treasure[0], treasure[1], 1])
        if obstacles != None:
            for obstacle in obstacles:
                self.items.append([obstacle[0], obstacle[1], 2])
        print("World initialized, simulator SHA1 checksum is", \
              hashlib.sha1(open("simulator.py", "r").read().encode("UTF-8")).hexdigest())
        
    
    def __register__(self, x, y, direction):
        """
        DO NOT USE THIS FUNCTION! USE Robot CONSTRUCTOR (e.g., Robot(x, y, direction) !
        
        Registers/creates a robot into the world
        
        Args:
            x: x coordinate (0 <= x < width)
            y: y coordinate (0 <= x < height)
            direction: robot facing direction 
                       (0 <= direction < 8 (i.e., 0 = north, 4 = south))
            
        Returns:
            The robot ID if successful
        """
        if type(x) == int and type(y) == int and type(direction) == int and \
        x >= 0 and x < self.width and y >= 0 and  y < self.height and \
        direction >= 0 and direction < 8:
            self.robots.append([x, y, direction, 0, [], self.endurance])
            return len(self.robots)-1
        raise RegistrationException
        
    def tick(self):
        """
        Simulate the world one time unit forward
        
        Raises:
            EndOfTheWorldException: if a robot crashes into a wall or collides with another robot
        """
        time.sleep(self.sleep_time)
        self.time += 1
        print("[Turn " + str(self.time) + "] Tick tock...")
        directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        for i in range(len(self.robots)):
            self.robots[i][2] = (self.robots[i][2] + self.robots[i][3]) % 8
            self.robots[i][3] = 0
            self.robots[i][0] += directions[self.robots[i][2]][0]
            self.robots[i][1] += directions[self.robots[i][2]][1]
            if self.robots[i][0] < 0 or self.robots[i][0] >= self.width or \
            self.robots[i][1] < 0 or self.robots[i][1] >= self.height:
                self.robots = []
                raise RobotWallCrashException # A robot crashed into a wall! Simulation over!
            for j in range(len(self.robots)):
                if i != j:
                    if self.robots[i][0] == self.robots[j][0] and self.robots[i][1] == self.robots[j][1]:
                        self.robots = []
                        raise RobotCollisionException # A robot crashed into another robot! Simulation over!
            for j in range(len(self.items)):
                if self.robots[i][0] == self.items[j][0] and self.robots[i][1] == self.items[j][1]:
                    if self.items[j][2] == 1:
                        self.robots = []
                        raise RobotFoundTreasureException # A robot found the treasure! You win!
                    elif self.items[j][2] == 2:
                        self.robots = []
                        raise RobotObjectCrashException # A robot crashed into an object!
            if random.random() > self.reliability:
                print("*glug-glug-glug* Oil leak detected!")
                self.items.append([self.robots[i][0], self.robots[i][1], 2]) 
    
    def __detect__(self, ID, direction):
        directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
        for i in range(1, 3):
            check_x = self.robots[ID][0] + (directions[direction][0] * i)
            check_y = self.robots[ID][1] + (directions[direction][1] * i)
            for robot in self.robots:
                if robot[0] == check_x and robot[1] == check_y:
                    return (i, robot[2]) # Robot detected
            for item in self.items:
                if check_x == item[0] and check_y == item[1]:
                    if item[2] == 1:
                        return (i, -3) # Detected treasure
                    elif item[2] == 2:
                        return (i, -2) # Detected obstacle
            if check_x < 0 or check_y < 0 or check_x >= self.width or check_y >= self.height:
                return (i, -1) # Wall detected
        return None
        
    
    def __turn__(self, ID, direction):
        if abs(direction) == 2:
            if self.robots[ID][5] > 0:
                print("*creak*shriek* The cogs rattle and tires squeal as the robot frantically turns!")
                self.robots[ID][3] = direction
                self.robots[ID][5] -= 1
                return
            else:
                if direction > 0:
                    direction -= 1
                else:
                    direction += 1
        if abs(direction) <= 2:
            self.robots[ID][3] = direction
            
            
    def __compass__(self, ID):
        return self.robots[ID][2]
        
    def print_state(self):
        """
        Prints the state of the world
        """
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]
        icons = ["^", "/", ">", "\\", "|", "/", "<", "\\"] # NON-UNICODE, uncomment if problems
        #icons = [chr(0x2191), chr(0x2197), chr(0x2192), chr(0x2198), \
        #         chr(0x2193), chr(0x2199), chr(0x2190), chr(0x2196)]
        for robot in self.robots:
            grid[robot[1]][robot[0]] = icons[(robot[2]+robot[3]) % 8]
        for item in self.items:
            if item[2] == 1:
                grid[item[1]][item[0]] = "O"
            elif item[2] == 2:
                grid[item[1]][item[0]] = "*"
        print("-"*(self.width+2))
        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                print(grid[i][j], end="")
            print("|")
        print("-"*(self.width+2))
        
    def __iadd__(self, other):
        for _ in range(other):
            self.tick()
        return self
        
class Agent:
    """
    Use this class as a superclass for your robot!
    """
    ID = 0
    
    
    def __init__(self, world, x, y, direction):
        """
        Creates and registers the robot into the world
        
        Args:
            x: x coordinate (0 <= x < width)
            y: y coordinate (0 <= x < height)
            direction: robot facing direction (0 <= direction < 8 (i.e., 0 = north, 4 = south))
            
        Returns:
            None
        
        Raises:
            RegistrationException if unsuccessful
        """
        self.ID = world.__register__(x, y, direction)
    
    def detect(self, world, direction):
        """
        Detects obstacles/treasure in the direction given
        
        Args:
            world: the instance of the world
            direction: the direction you want to check
            
        Returns:
            A tuple with distance and movement direction of the object (e.g., (2, 2) = distance two, robot moving east)  
            (wall "direction" is -1)
            (obstacle "direction" is -2)
            (treasure "direction" is -3)
            
        """
        return world.__detect__(self.ID, direction)
        
     
    def turn(self, world, direction):
        """
        Turns the robot into specified direction.
        
        Args:
            world: the instance of the world
            direction: turn direction  -2 = hard left (-90 degrees), -1 = left (-45 degrees), 1 = right (45 degrees), 2 = hard right(+90 degrees)
            
        Returns:
            None
        """
        world.__turn__(self.ID, int(direction))
        
        
    def compass(self, world):
        """
        Returns the current heading
        
        Returns:
            Current heading (0..7)
        """
        return world.__compass__(self.ID)

if __name__ == "__main__":
    print("You are supposed to import this file via 'import simulator', not run it!")