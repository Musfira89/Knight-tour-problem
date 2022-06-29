from tkinter import *
import tkinter
import sys
from collections import deque
 
 
# A queue node used in BFS
class Node:
    # (x, y) represents chessboard coordinates
    # `dist` represents its minimum distance from the source
    def _init_(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
    # As we are using `Node` as a key in a dictionary,
    # we need to override the `_hash()` and `eq_()` function
    def _hash_(self):
        return hash((self.x, self.y, self.dist))
 
    def _eq_(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
 
# Check if (x, y) is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)
 
 
# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def findShortestDistance(src, dest, N):
 
    # set to check if the matrix cell is visited before or not
    visited = set()
 
    # create a queue and enqueue the first node
    q = deque()
    q.append(src)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
 
        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist
 
        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)
 
            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(len(row)):
                # get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]
 
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
 
    # return infinity if the path is not possible
    return sys.maxsize
###### 
# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("800x450")


def cal_sum():




    t1=int(a.get())
    t2=int(b.get())
    N = 8                # N x N matrix

    src = Node(0, t1)    # source coordinates
    dest = Node(t2, 0)   # destination coordinates
 
    ans=findShortestDistance(src, dest, N)
    label.config(text=ans)


# Create an Entry widget


Label(win, text="Enter source place between 1 to 7", font=('Calibri 20')).pack(padx=100,pady=20, ipady=20,ipadx=30)
a=Entry(win, width=20)
a.pack()
Label(win, text="Enter destination place btw 1 to 7", font=('Calibri 20')).pack(padx=100,pady=20, ipady=20,ipadx=30)
b=Entry(win, width=20)
b.pack()

label=Label(win, text="Min steps : ", font=('Calibri 20'))
label.pack(pady=20)

Button(win, text="Calculate Sum", command=cal_sum).pack()

win.mainloop()

######
 
if __name__ == '_main_':
 
    cal_sum()