def frequency(li):
    l = len(li)
    visited = [False] * l   
    for i in range(l):
        if visited[i] == True:
            continue
        count = 1   
        for j in range(i+1, l):
            if li[i] == li[j]:
                count += 1
                visited[j] = True   
        print(f"{li[i]} -> {count}")
li = list(map(int, input("Enter elements: ").split()))
frequency(li)
