if __name__ == "__main__":
    iterations = list(map(int,input().split()))
    type_of_server = dict()
    i = 0
    while i < iterations[0]:
        name, ip = input().split()
        type_of_server[ip] = name
        i+=1
    
    j = 0
    while j < iterations[1]:
        server, ips = input().split()
        if ips[:-1] in type_of_server:
            print(f"{server} {ips} #{type_of_server[ips[:-1]]}")
        j+=1