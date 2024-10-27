import math
import copy
class PointDatabase:
    def __init__(self, pointlist):
        self.n=len(pointlist)
        pointlist.sort(key=lambda x: x[1])

        self.list=[]
        self.list.append(pointlist)
        x=1
        while(x*2<self.n):
            kaju=[0]*(self.n)
            z=0                         

            store=x
            x=x*2
            i=1
            y=0
            while(y+x<=self.n):
                j=y
                k=(y+x//2)
                while(j<y+store and k<y+x):
                    if(self.list[-1][j]<self.list[-1][k]):
                        kaju[z]=(self.list[-1][j])
                        j+=1
                    elif(self.list[-1][j]>self.list[-1][k]):
                        kaju[z]=self.list[-1][k]
                        k+= 1
                    else:
                        kaju[z]=(self.list[-1][j])
                        kaju[z]=(self.list[-1][k])
                        k+=1
                        j+=1
                        z+=1
                    z+=1
                if(j<y+store):
                    for q in range(j,y+store):
                        kaju[z]=(self.list[-1][q])
                        z+=1
                else:
                    for q in range(k,y+x):
                        kaju[z]=(self.list[-1][q])
                        z+=1

                y=y+x
            for z in range(y,self.n):
                kaju[z]=(self.list[-1][z])
            self.list.append(kaju)
        self.list.append(self.list[-1].copy())
        self.list[-1].sort(key=lambda x: x[0])
        """for i in range(len(self.list)):
            print(self.list[i])"""
    def binarystart(self,key,r,l,index,numb):
        while(r<=l):
            mid = int((r + l) / 2)
            if (key <= self.list[numb][mid][index] and key > self.list[numb][mid - 1][index]):
                return mid
            elif (key < self.list[numb][mid][index]):
                l=mid-1
            else:
                r=mid+1
        return -1

    def binaryend(self,key,r,l,index,numb):
        while(r<=l):
            mid = int((r + l) / 2)
            if (key>= self.list[numb][mid][index] and key<self.list[numb][mid+1][index]):
                return mid
            elif (key>self.list[numb][mid][index]):
                r=mid+1
            else:
                l=mid-1
        return -1

    def maxpower(self,n):
        m=0
        if n==0:
            return int(math.log2(self.n))
        while(n%2==0):
            n=n//2
            m+=1
        return m

    def searchNearby(self, q, d):
        if(self.n==0):
            return []

        output=[]
        if(q[1]-d<=self.list[0][0][1]):
            start=0
        else:
            start=self.binarystart(q[1]-d,1,self.n-1,1,0)

        if (q[1]+d >= self.list[0][-1][1]):
            end = self.n-1
        else:
            end = self.binaryend(q[1]+d, 0, self.n - 2,1,0)

        if(start==-1 or end==-1 or start>end):
            return output
        while(start<=end):
            k=self.maxpower(start)
            while(start+pow(2,k)-1>end):
                k=k-1
            fend=start+pow(2,k)-1

            if (q[0]-d <= self.list[k][start][0]):
                begin = start
        
            else:
                begin = self.binarystart(q[0] - d, start+1, fend, 0, k)

            if (q[0] + d >= self.list[k][fend][0]):
                stop = fend
            else:
                stop = self.binaryend(q[0] + d, start, fend - 1, 0, k)
            #print("idl",self.list[k],k,begin,stop)
            if(begin<=stop and begin!=-1 and stop!=-1):
                for bc in range(begin,stop+1):
                    output.append(self.list[k][bc])
            start=fend+1

        return output






""""pointDbObject = PointDatabase([(32, 72), (68, 52), (10, 59), (71, 85), (99, 96), (86, 7), (82, 65), (29, 50), (96, 49), (52, 94), (56, 93), (88, 78), (75, 98), (26, 56), (34, 26), (43, 55), (70, 80), (22, 30), (60, 47), (39, 70)])
print(pointDbObject.searchNearby((18,69), 69.5))
print(pointDbObject.searchNearby((4,8), 2))
print(pointDbObject.searchNearby((10,2), 1.5))"""

"""pointDbObject = PointDatabase([(1,6), (2,4), (3,7), (4,9), (5,1), (6,3), (7,8), (8,10),(9,2), (10,5)])
print(pointDbObject.searchNearby((5,5), 1))
print(pointDbObject.searchNearby((4,8), 2))
print(pointDbObject.searchNearby((10,2), 1.5))"""











