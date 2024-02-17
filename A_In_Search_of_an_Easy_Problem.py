if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split()))
    if sum(nums) > 0:
        print("HARD")
    else:
        print("EASY")