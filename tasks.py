# Patika - Veri Analizi Patikası Python Temel dersi sonu proje ödevi

# Task 1

input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten1(A):
    for i in A:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

final_list = list(flatten(input1))
print(final_list)

# Task 2 

input2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse1(B):
    input2.reverse()
    for i in B:
        if isinstance(i, list):
            i.reverse()
        else:
            pass
    return input2

print(reverse1(input2))
