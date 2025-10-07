n = int(input().strip())

count_offline = 0
count_online = 0

for _ in range(n):
    data = input().split()
    
    format_str = data[-1]
    
    if format_str == "True":
        count_offline += 1
    else:
        count_online += 1

print(f"{count_offline} {count_online}")