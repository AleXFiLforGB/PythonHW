def find_min(a):
    min = a[0]
    for i in a: 
        if i < min: min = i
    return min

def find_max(a):
    max = a[0]
    for i in a:
        if i > max: max = i 
    return max

def diff_between_min_max (lst):
    diff = find_max(lst) - find_min(lst)
    return diff

def transform_to_binary(a, system = 2):
    a_t = ''
    while a > 0:
        a_t += str (a%system)
        a//=system
    return a_t
print (transform_to_binary(3))