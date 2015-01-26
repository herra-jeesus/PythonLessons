"""
Ülesanne 7 - OOP
Juhend: https://courses.cs.ttu.ee/w/images/d/da/2014_Loeng_7_-_OOP.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

from simulator import *
import random

class Robot(Agent):

    def reason(self, world):
        directions = {0: 'N', 1: 'NE', 2: 'E', 3: 'SE', 4: 'S', 5: 'SW', 6: 'W', 7: 'NW'}
        directionsLookupTable = { # current direction | desired direction : turn value
            # North
            ('N', 'N'): 0, ('N', 'NE'): 1, ('N', 'E'): 2, ('N', 'SE'): 2,
            ('N', 'S'): 2, ('N', 'SW'): -2, ('N', 'W'): -2, ('N', 'NW'): -1,

            # North-East
            ('NE', 'N'): -1, ('NE', 'NE'): 0, ('NE', 'E'): 1, ('NE', 'SE'): 2,
            ('NE', 'S'): 2, ('NE', 'SW'): -2, ('NE', 'W'): -2, ('NE', 'NW'): -2,

            # East
            ('E', 'N'): -2, ('E', 'NE'): -1, ('E', 'E'): 0, ('E', 'SE'): 1,
            ('E', 'S'): 2, ('E', 'SW'): 2, ('E', 'W'): 2, ('E', 'NW'): -2,

            # South-East
            ('SE', 'N'): -2, ('SE', 'NE'): -2, ('SE', 'E'): -1, ('SE', 'SE'): 0,
            ('SE', 'S'): 1, ('SE', 'SW'): 2, ('SE', 'W'): 2, ('SE', 'NW'): -2,

            # South
            ('S', 'N'): 2, ('S', 'NE'): -2, ('S', 'E'): -2, ('S', 'SE'): -1,
            ('S', 'S'): 0, ('S', 'SW'): 1, ('S', 'W'): 2, ('S', 'NW'): 2,

            # South-West
            ('SW', 'N'): 2, ('SW', 'NE'): 2, ('SW', 'E'): -2, ('SW', 'SE'): -2,
            ('SW', 'S'): -1, ('SW', 'SW'): 0, ('SW', 'W'): 1, ('SW', 'NW'): 2,

            # West
            ('W', 'N'): 2, ('W', 'NE'): 2, ('W', 'E'): 2, ('W', 'SE'): -2,
            ('W', 'S'): -2, ('W', 'SW'): -1, ('W', 'W'): 0, ('W', 'NW'): 1,

            # North-West
            ('NW', 'N'): 1, ('NW', 'NE'): 2, ('NW', 'E'): 2, ('NW', 'SE'): 2,
            ('NW', 'S'): -2, ('NW', 'SW'): -2, ('NW', 'W'): -1, ('NW', 'NW'): 0,
        }
        robotCollisionLookupTable = { # current robot direction | other robot direction | robot location | distance : unsafe direction
            # North
            ('N', 'NE', 'W', 1): 0, ('N', 'E', 'NW', 1): 0, ('N', 'S', 'N', 1): 0,
            ('N', 'S', 'N', 2): 0, ('N', 'W', 'NE', 1): 0, ('N', 'NW', 'E', 1): 0,

            # North-East
            ('NE', 'N', 'E', 1): 1, ('NE', 'E', 'N', 1): 1, ('NE', 'SE', 'N', 2): 1,
            ('NE', 'SW', 'NE', 1): 1, ('NE', 'SW', 'NE', 2): 1, ('NE', 'NW', 'E', 2): 1,

            # East
            ('E', 'N', 'SE', 1): 2, ('E', 'NE', 'S', 1): 2, ('E', 'SE', 'N', 1): 2,
            ('E', 'S', 'NE', 1): 2, ('E', 'W', 'E', 1): 2, ('E', 'W', 'E', 2): 2,

            # South-East
            ('SE', 'NE', 'S', 2): 3, ('SE', 'E', 'S', 1): 3, ('SE', 'S', 'E', 1): 3,
            ('SE', 'SW', 'E', 2): 3, ('SE', 'NW', 'SE', 1): 3, ('SE', 'NW', 'SE', 2): 3,

            # South
            ('S', 'N', 'S', 1): 4, ('S', 'N', 'S', 2): 4, ('S', 'E', 'SW', 1): 4,
            ('S', 'SE', 'W', 1): 4, ('S', 'SW', 'E', 1): 4, ('S', 'W', 'SE', 1): 4,

            # South-West
            ('SW', 'NE', 'SW', 1): 5, ('SW', 'NE', 'SW', 2): 5, ('SW', 'SE', 'W', 2): 5,
            ('SW', 'S', 'W', 1): 5, ('SW', 'W', 'S', 1): 5, ('SW', 'NW', 'S', 2): 5,

            # West
            ('W', 'N', 'SW', 1): 6, ('W', 'E', 'W', 1): 6, ('W', 'E', 'W', 2): 6,
            ('W', 'S', 'NW', 1): 6, ('W', 'SW', 'N', 1): 6, ('W', 'NW', 'S', 1): 6,

            # North-West
            ('NW', 'N', 'W', 1): 7, ('NW', 'NE', 'W', 2): 7, ('NW', 'SE', 'NW', 2): 7,
            ('NW', 'SE', 'NW', 2): 7, ('NW', 'SW', 'N', 2): 7, ('NW', 'W', 'N', 1): 7,
        }

        random.seed()
        info = []
        unsafeDirections = set()
        turnDirection = None
        treasureDirection = None
        robotDirection = self.compass(world)

        """
        Look at all directions for
        """
        for direction in range(0, 8):
            info = self.detect(world, direction)

            if info == None: # nothing found
                pass
            elif info[1] == -1: # wall detected in that direction
                if info[0] == 1: # wall is one unit away
                    unsafeDirections.add(direction)
                elif info[0] == 2: # wall is two units away; 4 special cases
                    if robotDirection == 1 and direction == 1: # north-east corner
                        info1 = self.detect(world, 0) # north
                        info2 = self.detect(world, 2) # east
                        if info1 == None or info2 == None:
                            pass
                        elif info1[0] == 2 and info2[0] == 2:
                            unsafeDirections.add(direction)
                    elif robotDirection == 3 and direction == 3: # south-east corner
                        info1 = self.detect(world, 4) # south
                        info2 = self.detect(world, 2) # east
                        if info1 == None or info2 == None:
                            pass
                        elif info1[0] == 2 and info2[0] == 2:
                            unsafeDirections.add(direction)
                    elif robotDirection == 5 and direction == 5: # south-west corner
                        info1 = self.detect(world, 4) # south
                        info2 = self.detect(world, 6) # west
                        if info1 == None or info2 == None:
                            pass
                        elif info1[0] == 2 and info2[0] == 2:
                            unsafeDirections.add(direction)
                    elif robotDirection == 7 and direction == 7: # north-west corner
                        info1 = self.detect(world, 0) # north
                        info2 = self.detect(world, 6) # west
                        if info1 == None or info2 == None:
                            pass
                        elif info1[0] == 2 and info2[0] == 2:
                            unsafeDirections.add(direction)
            elif info[1] == -2: # obstacle in that direction
                if info[0] == 1: # obstacle is one unit away
                    unsafeDirections.add(direction)
            elif info[1] == -3: # treasure in that direction
                treasureDirection = direction
            elif info[1] in range(0, 8): # robot in that direction
                if info[0] == 1: # robot is one unit away
                    unsafeDirections.add(direction)

                # check for robot collision
                _robotDirection = directions[robotDirection]
                _robotDirection2 = directions[info[1]]
                lookupTuple = (_robotDirection, _robotDirection2, directions[direction], info[0])
                if lookupTuple in robotCollisionLookupTable:
                    unsafeDirections.add(robotCollisionLookupTable[lookupTuple])

        """
        Make turn decision
        """
        if treasureDirection != None and treasureDirection not in unsafeDirections:
            _robotDirection = directions[robotDirection]
            _treasureDirection = directions[treasureDirection]
            turnDirection = directionsLookupTable[(_robotDirection, _treasureDirection)]
            # calculate effective direction
            effectiveDirection = (robotDirection + turnDirection) % 8
            if effectiveDirection < 0: effectiveDirection += 8
            while effectiveDirection in unsafeDirections:
                turnDirection = random.randint(0, 7) # random direction that is safe
                _robotDirection = directions[robotDirection]
                _turnDirection = directions[turnDirection]
                turnDirection = directionsLookupTable[(_robotDirection, _turnDirection)]
                # calculate effective direction
                effectiveDirection = (robotDirection + turnDirection) % 8
                if effectiveDirection < 0: effectiveDirection += 8

        elif robotDirection in unsafeDirections: # robot is moving towards unsafe direction, change direction!
            effectiveDirection = robotDirection
            while effectiveDirection in unsafeDirections:
                turnDirection = random.randint(0, 7) # random direction that is safe
                _robotDirection = directions[robotDirection]
                _turnDirection = directions[turnDirection]
                turnDirection = directionsLookupTable[(_robotDirection, _turnDirection)]
                # calculate effective direction
                effectiveDirection = (robotDirection + turnDirection) % 8
                if effectiveDirection < 0: effectiveDirection += 8

        if turnDirection != None:
            self.turn(world, turnDirection)