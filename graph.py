def BFS(graph , start):
    queue = [start]
    visited = {start}
    while queue:
        vertex = queue.pop(0)
        for ne in graph[vertex]:
            if ne not in visited:
                visited.add(ne)
                queue.append(ne)


    return visited

def DFS(graph , start , visited):
    visited[start] = True
    print (start)
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph , ne , visited)

def sort1(A):
    B = [0] *len(A)
    for j in range(len(A)):
        min=A[0]
        K=0
        for i in range(1,len(A)):
            if A[i] < min:
                min = A[i]
                k = i
        B[j] = min
        A[k] = float("lnf")
    return B 

def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1] , A[j]
