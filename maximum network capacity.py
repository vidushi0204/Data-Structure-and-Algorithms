import math

#HEAP 
def swap(heap,i,j):
    heap[i],heap[j]=heap[j],heap[i]
def upheap(heap,j):
    parent=(j-1)//2
    if(j>0 and heap[j]>heap[parent]):
        swap(heap,j,parent)
        upheap(heap,parent)
def downheap(heap,j):
    if (2*j+1<len(heap)):
        left=2*j+1
        bigchild=left
        if (2*j+2<len(heap)):
            right=2*j+2
            if(heap[right][0]>heap[left][0]):
                bigchild=right
        if(heap[bigchild][0]>heap[j][0]):
            swap(heap,j,bigchild)
            downheap(heap,bigchild)
def removemax(list):
    swap(list,0,len(list)-1)
    list.pop()
    downheap(list,0)


#ADJACENCY LIST
def adjlist(n,links):
    adj=[]
    for i in range(n):
        adj.append([])
    for x in links:
        adj[x[0]].append((x[2],x[1]))
        adj[x[1]].append((x[2],x[0]))
    return adj

#MAIN FUNCTION
def findMaxCapacity(n,links,s,t):
    capacity=[-1]*n
    prev=[None]*n
    list=[(math.inf,s)]

    adj=adjlist(n,links)
    capacity[s]=math.inf

    while(len(list)):
        u=list[0][1]
        removemax(list)
        
        for v in adj[u]:
            w=min(capacity[u],v[0])
            if w>capacity[v[1]]:
                capacity[v[1]]=w
                prev[v[1]]=u
                list.append((w,v[1]))
                upheap(list,len(list)-1)
                
        if(list[0][1]==t):
            break
        
    path=[t]
    q=t
    while(q!=s):
        path.append(prev[q])
        q=prev[q]
    path.reverse()

    return(capacity[t],path)


# findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1)
# findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3)
# findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3)
# findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2)
# findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5)