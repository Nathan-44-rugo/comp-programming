if __name__ == "__main__":
    n = int(input())
    percentages = list(map(int, input().split()))
    total_percentage = sum(percentages) / n
    print(total_percentage)