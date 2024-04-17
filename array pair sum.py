arr = [1, 3, 2, 2]
target = 4
if len(arr) < 2:
    print([])
seen = set()
output = set()
for num in arr:
    complement = target - num
    if complement in seen:        
        output.add((min(num, complement), max(num, complement)))
    seen.add(num)
print(list(output))
