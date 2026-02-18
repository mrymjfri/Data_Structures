
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
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph , ne , visited)
    return visited



def sort1(A):
    B = [0] * len(A)

    for j in range(len(A)):
        min_val = A[0]
        k = 0

        for i in range(1, len(A)):
            if A[i] < min_val:
                min_val = A[i]
                k = i

        B[j] = min_val
        A[k] = float("inf")

    return B



def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A



def selection_sort(A):
    for j in range(len(A)):
        min_index = j
        for i in range(j+1, len(A)):
            if A[i] < A[min_index]:
                min_index = i
        A[j], A[min_index] = A[min_index], A[j]
    return A



def quick_sort(A , low , high):
    if low < high:
        pi = partition(A , low , high)
        quick_sort(A , low , pi-1)
        quick_sort(A , pi+1 , high)

def partition(A , low , high):
    pivot = A[high]
    i = low-1

    for j in range(low , high):
        if A[j] < pivot:
            i += 1
            A[i],A[j] = A[j],A[i]

    A[i+1],A[high] = A[high],A[i+1]
    return i+1



def bucket_sort(A):
    if len(A) == 0:
        return A

    min_value = min(A)
    max_value = max(A)

    bucket_count = len(A)
    buckets = [[] for _ in range(bucket_count)]

    for num in A:
        index = int((num - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(num)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array
    
