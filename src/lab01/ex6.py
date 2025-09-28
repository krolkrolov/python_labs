n = int(input().strip())
count_offline = 0
count_online = 0

for _ in range(n):
    data = input().split()
    
    if len(data) >= 4:
        format_str = data[-1]
        if format_str == "True":
            count_offline += 1
        elif format_str == "False":
            count_online += 1

print(f"{count_offline} {count_online}")