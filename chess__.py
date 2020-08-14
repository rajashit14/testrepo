def explore(sx,sy,tx,ty,n,m):
    marked=[[0 for i in range(n)] for j in range (m)]
    marked[sx][sy]=1
    queue=[(sx,sy)]
    while queue!=[]:
        (ax,ay)=queue.pop()
        for (nx,ny) in neighbours((ax,ay)):
            if (marked[nx][ny])!=1:
                marked[nx][ny]=1
                queue.insert(0,(nx,ny))
    return(marked[tx,ty])

n=int(input())
m=int(input())
sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(explore(sx,sy,tx,ty,n,m))