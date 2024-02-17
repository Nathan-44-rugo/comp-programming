if __name__ == "__main__":
    n = int(input())
    net_entry_list = []
    for _ in range(n):
        a,b = input().split()
        net_entry_list.append(a)
        net_entry_list.append(b)
    max_pass = list()
    increment = 0
    for i in range(1,len(net_entry_list)-1,2):
        first = increment + int(net_entry_list[i])
        max_pass.append(first)
        increment = first - int(net_entry_list[i+1])
    print(max(max_pass))
