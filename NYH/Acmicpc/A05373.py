import sys

class Cube:

    def __init__(self):
        self.top = [
            ["w","w","w"],
            ["w","w","w"],
            ["w","w","w"]
        ]
        self.down = [
            ["y","y","y"],
            ["y","y","y"],
            ["y","y","y"]
        ]

        self.front = [
            ["r","r","r"],
            ["r","r","r"],
            ["r","r","r"]
        ]

        self.back = [
            ["o", "o", "o"],
            ["o", "o", "o"],
            ["o", "o", "o"]
        ]

        self.left = [
            ["g","g","g"],
            ["g","g","g"],
            ["g","g","g"]
        ]
        self.right = [
            ["b","b","b"],
            ["b","b","b"],
            ["b","b","b"]
        ]

    def clockwise(self, pos):
        if pos == 'U':
            self.top[0][0] , self.top[0][2],\
                self.top[2][2], self.top[2][0]\
                    = self.top[2][0], self.top[0][0],\
                    self.top[0][2], self.top[2][2]
            self.top[0][1], self.top[1][2],\
                self.top[2][1], self.top[1][0]\
                    = self.top[1][0], self.top[0][1],\
                        self.top[1][2], self.top[2][1]
            self.left[0], self.back[0], self.right[0], self.front[0] \
                = [item for item in self.front[0]], [item for item in self.left[0]]\
                , [item for item in self.back[0]], [item for item in self.right[0]]
        elif pos == 'D':
            self.down[0][0] , self.down[0][2]\
            , self.down[2][2], self.down[2][0]\
                = self.down[2][0], self.down[0][0]\
                , self.down[0][2], self.down[2][2]
            self.down[0][1], self.down[1][2]\
            , self.down[2][1], self.down[1][0]\
                = self.down[1][0], self.down[0][1]\
                , self.down[1][2], self.down[2][1]

            self.front[2], self.right[2]\
            , self.back[2], self.left[2] =\
            [item for item in self.left[2]], [item for item in self.front[2]] \
            , [item for item in self.right[2]], [item for item in self.back[2]]
        elif pos == 'L':
            self.left[0][0] , self.left[0][2],\
                self.left[2][2], self.left[2][0]\
                    = self.left[2][0], self.left[0][0]\
                    , self.left[0][2], self.left[2][2]
            self.left[0][1], self.left[1][2],\
                self.left[2][1], self.left[1][0]\
                    = self.left[1][0], self.left[0][1],\
                        self.left[1][2], self.left[2][1]
            for i in range(3):
                self.top[i][0], self.front[i][0] \
                , self.down[2 - i][2], self.back[2 - i][2]\
                    = self.back[2 - i][2], self.top[i][0]\
                        , self.front[i][0], self.down[2 - i][2]
        elif pos == 'R':
            self.right[0][0] , self.right[0][2],\
                self.right[2][2], self.right[2][0]\
                    = self.right[2][0], self.right[0][0]\
                    , self.right[0][2], self.right[2][2]
            self.right[0][1], self.right[1][2],\
                self.right[2][1], self.right[1][0]\
                    = self.right[1][0], self.right[0][1],\
                        self.right[1][2], self.right[2][1]
            for i in range(3):
                self.top[i][2], self.front[i][2], \
                self.down[2 - i][0], self.back[2 - i][0] \
                    = self.front[i][2], self.down[2 - i][0]\
                    , self.back[2 - i][0], self.top[i][2]
        elif pos =='F':
            self.front[0][0] , self.front[0][2],\
                self.front[2][2], self.front[2][0]\
                    = self.front[2][0], self.front[0][0]\
                    , self.front[0][2], self.front[2][2]
            self.front[0][1], self.front[1][2],\
                self.front[2][1], self.front[1][0]\
                    = self.front[1][0], self.front[0][1],\
                        self.front[1][2], self.front[2][1]

            for i in range(3):

                self.right[i][0], self.top[2][i],\
                    self.left[2 - i][2], self.down[2][i] = \
                    self.top[2][i], self.left[2 - i][2]\
                    , self.down[2][i], self.right[i][0]
        elif pos =='B':
            self.back[0][0] , self.back[0][2],\
                self.back[2][2], self.back[2][0]\
                    = self.back[2][0], self.back[0][0]\
                    , self.back[0][2], self.back[2][2]
            self.back[0][1], self.back[1][2],\
                self.back[2][1], self.back[1][0]\
                    = self.back[1][0], self.back[0][1],\
                        self.back[1][2], self.back[2][1]
            for i in range(3):
                self.top[0][i], self.right[i][2]\
                    ,self.down[0][i], self.left[2 - i][0]= \
                    self.right[i][2], self.down[0][i]\
                    , self.left[2 - i][0], self.top[0][i] 

    def counter_clockwise(self, pos):
        if pos == 'U':
            
            self.top[0][0] , self.top[0][2],\
                self.top[2][2], self.top[2][0]\
                    = self.top[0][2], self.top[2][2],\
                    self.top[2][0], self.top[0][0]

            self.top[0][1], self.top[1][2],\
                self.top[2][1], self.top[1][0]\
                    = self.top[1][2], self.top[2][1],\
                        self.top[1][0], self.top[0][1]
            
            self.left[0], self.back[0], self.right[0], self.front[0] \
                 = [item for item in self.back[0]], [item for item in self.right[0]]\
                , [item for item in self.front[0]], [item for item in self.left[0]]
        elif pos == 'D':
            self.down[0][0] , self.down[0][2],\
                self.down[2][2], self.down[2][0]\
                    = self.down[0][2], self.down[2][2],\
                    self.down[2][0], self.down[0][0]

            self.down[0][1], self.down[1][2],\
                self.down[2][1], self.down[1][0]\
                    = self.down[1][2], self.down[2][1],\
                        self.down[1][0], self.down[0][1]

            self.front[2], self.right[2], self.back[2], self.left[2] \
                = [item for item in self.right[2]], [item for item in self.back[2]], [item for item in self.left[2]], [item for item in self.front[2]]
        elif pos == 'L':
            self.left[0][0] , self.left[0][2],\
                self.left[2][2], self.left[2][0]\
                    = self.left[0][2], self.left[2][2],\
                    self.left[2][0], self.left[0][0]

            self.left[0][1], self.left[1][2],\
                self.left[2][1], self.left[1][0]\
                    = self.left[1][2], self.left[2][1],\
                        self.left[1][0], self.left[0][1]
            for i in range(3):
                self.top[i][0], self.front[i][0] \
                , self.down[2 - i][2], self.back[2 - i][2]\
                    = self.front[i][0], self.down[2 - i][2]\
                        , self.back[2 - i][2], self.top[i][0]
        elif pos == 'R':
            self.right[0][0] , self.right[0][2],\
                self.right[2][2], self.right[2][0]\
                    = self.right[0][2], self.right[2][2],\
                    self.right[2][0], self.right[0][0]

            self.right[0][1], self.right[1][2],\
                self.right[2][1], self.right[1][0]\
                    = self.right[1][2], self.right[2][1],\
                        self.right[1][0], self.right[0][1]
            for i in range(3):
                self.front[i][2], self.top[i][2] \
                , self.back[2 - i][0], self.down[2 - i][0]\
                    = self.top[i][2], self.back[2 - i][0]\
                    , self.down[2 - i][0], self.front[i][2]
        elif pos =='F':
            self.front[0][0] , self.front[0][2],\
                self.front[2][2], self.front[2][0]\
                    = self.front[0][2], self.front[2][2],\
                    self.front[2][0], self.front[0][0]

            self.front[0][1], self.front[1][2],\
                self.front[2][1], self.front[1][0]\
                    = self.front[1][2], self.front[2][1],\
                        self.front[1][0], self.front[0][1]

            for i in range(3):
                self.right[i][0], self.top[2][i]\
                    , self.left[2 - i][2], self.down[2][i]  = \
                    self.down[2][i], self.right[i][0]\
                    ,self.top[2][i], self.left[2 - i][2]

        elif pos =='B':
            self.back[0][0] , self.back[0][2],\
                self.back[2][2], self.back[2][0]\
                    = self.back[0][2], self.back[2][2],\
                    self.back[2][0], self.back[0][0]

            self.back[0][1], self.back[1][2],\
                self.back[2][1], self.back[1][0]\
                    = self.back[1][2], self.back[2][1],\
                        self.back[1][0], self.back[0][1]

            for i in range(3):
                self.right[i][2], self.down[0][i]\
                , self.left[2 - i][0], self.top[0][i]  = \
                    self.top[0][i], self.right[i][2]\
                    , self.down[0][i] , self.left[2 - i][0]\
                        

def input():
    return sys.stdin.readline().rstrip()

def solution(rotates):
    cube = Cube()
    for rotate in rotates:
        if rotate[1] == '+':
            cube.clockwise(rotate[0])
        elif rotate[1] == '-':
            cube.counter_clockwise(rotate[0])

    for top in cube.top:
        print("".join(top))
    

if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        n = int(input())
        rotates = list(map(str, input().split()))
        solution(rotates)