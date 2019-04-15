def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n   # n: unique integer in the array

print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
