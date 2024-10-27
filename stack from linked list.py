class Node:
    #define Node that stores data and address to the next node of LINKED LIST
    def __init__(self,data):
        self.data = data
        self.next = None      
class Stack: 
    #Implementation of STACK using LINKED LIST
    def __init__(self):
        #define head of empty stack
        self.head = None      
    def push(self,data):      
        if self.head == None:
            #if stack is empty, assign the data to head of stack
            self.head=Node(data)             
        else:
            #Add a node at top of stack and assign the data to it
            node = Node(data)
            node.next = self.head
            self.head = node    
    def pop(self):               
        self.head = self.head.next
    def top(self):          
        return self.head.data

def findPositionandDistance(P):
    #INPUT: string P
    #OUTPUT: List of length 4 -> [final X-coordinate, final Y-coordinate, final Z-coordinate, Total distance travelled]
    #ASSUMPTION: There is always an integer present before a bracket

    #initialisation
    output=[0,0,0,0]        #OUTPUT LIST
    stack=Stack()           #STACK to store the coeefficients of brackets in the string
    i=0                     #counter from 0 to n-1
    number=0                    
    lastnum=1               
    n=len(P)                #length of string
    
    while(i<n):             #TERMINATION: when i increases to n
        if(P[i]=='+'):
            output[ord(P[i+1])-88]+=lastnum      #O(1) time
            output[3]+=lastnum                   #O(1) time
            i+=1                                 #O(1) time     
        elif(P[i]=='-'):    
            output[ord(P[i+1])-88]-=lastnum      #O(1) time
            output[3]+=lastnum                   #O(1) time
            i+=1                                 #O(1) time
        elif(ord(P[i])>=48 and ord(P[i])<=57):  
            number+=int(P[i])                    #O(1) time
            if(ord(P[i+1])>=48 and ord(P[i+1])<=57):
                number*=10                       #O(1) time
            else:                
                stack.push(number)               #O(1) time: element is added at the top of stack
                number=0                         #O(1) time
        elif(P[i]=='('):    
            lastnum*=stack.top()                 #O(1) time: element at the top of stack is accessed
        elif(P[i]==')'):   
            lastnum=int(lastnum//(stack.top()))  #O(1) time     
            stack.pop()                          #O(1) time: element is popped from the top of stack
        i+=1                                     #O(1) time
    
    return output

