
import math


def time_finder(time_previous,v_first,v_second,x_first,x_second,inf):
    if v_first-v_second<=0.0:
        return inf
    else:
        return time_previous+(x_second-x_first)/(v_first-v_second)

def swap(index1,index2,pos_heap):
    pos_heap[index1],pos_heap[index2]=pos_heap[index2],pos_heap[index1]

def check_swap(child,parent,list,pos_heap):
    if list[child]>list[parent]:
        return
    else:
        swap(list[child][1],list[parent][1],pos_heap)
        list[child],list[parent]=list[parent],list[child]
        heap_down(child,list,pos_heap)
        return

def heap_down(i,list,pos_heap):
    node1=2*i+1
    node2=2*i+2
    if list[node1]<list[node2]:
        check_swap(node1,i,list,pos_heap)
    else:
        check_swap(node2,i,list,pos_heap)

def heap_up(i,list,pos_heap):
    if i==0:
        return
    parent=(i-1)//2
    if list[i]<list[parent]:
        swap(list[parent][1],list[i][1],pos_heap)
        list[parent],list[i]=list[i],list[parent]
        heap_up(parent,list,pos_heap)
        return

def build_heap(list,pos_heap):
    for i in range(0,len(pos_heap)):
        heap_down(len(pos_heap)-1-i,list,pos_heap)

def collision_solver(m1,m2,v1,v2):
    v1_new=(m1-m2)*v1/(m1+m2)+2*m2*v2/(m1+m2)
    v2_new=2*m1*v1/(m1+m2)-(m1-m2)*v2/(m1+m2)
    return (v1_new,v2_new)

def listCollisions(M,x,v,m,T):
    list=[]
    pos_heap=[]
    coordinate = []
    velocity = []
    time_initial = []
    answer = []
    infinity=T+1
    for i in range(0,len(M)):
        pos_heap.append(i)
        coordinate.append(x[i])
        velocity.append(v[i])
        time_initial.append(0)
        if i==len(M)-1:
            list.append((infinity,i))
        else:
            list.append((time_finder(0.0,v[i],v[i+1],x[i],x[i+1],infinity),i))
    for i in range(0,len(M)+5):
        list.append((math.inf,len(M)))
    build_heap(list,pos_heap)
    for i in range(0,int(m)):
        t=list[0][0]
        if t>T:
            return answer
        number=list[0][1]
        coordinate[number]=coordinate[number]+velocity[number]*(t-time_initial[number])
        coordinate[number+1]=coordinate[number]
        temp=collision_solver(M[number],M[number+1],velocity[number],velocity[number+1])
        velocity[number]=temp[0]
        velocity[number+1]=temp[1]
        time_initial[number]=t
        time_initial[number+1]=t
        answer.append((t,number,coordinate[number]))
        dummy=list[0][1]
        list[0]=(infinity,dummy)
        heap_down(0,list,pos_heap)
        if number>0:
            new_time=time_finder(t,velocity[number-1],velocity[number],coordinate[number-1]+velocity[number-1]*(t-time_initial[number-1]),coordinate[number],infinity)
            index=pos_heap[number-1]
            list[index]=(new_time,list[index][1])
            heap_down(index,list,pos_heap)
            heap_up(index,list,pos_heap)
        if number+2<len(M):
            new_time=time_finder(t,velocity[number+1],velocity[number+2],coordinate[number+1],coordinate[number+2]+(t-time_initial[number+2])*velocity[number+2],infinity)
            index=pos_heap[number+1]
            list[index]=(new_time,list[index][1])
            heap_down(index,list,pos_heap)
            heap_up(index,list,pos_heap)

    return answer

