# def selection_sort(arr, n):
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# def bubble_sort(arr,n):
#     for i in range(n):
#         swap = 0
#         for j in range(1,n-i):
#             if arr[j-1] > arr[j]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#                 swap += 1
#         if swap == 0:
#             break
#     return arr

def insertion_sort(arr,n):
    for i in range(1,n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


arr = [64, 25, 12, 22, 11]
n = len(arr)
print(arr)
print(insertion_sort(arr, n))