# python3
import math   
class Heap:
    swap = []
    swaps = list(swap)
    
    
    def build_heap(heap, n):
        HeapSize = int(n // 2 -1)
        i = HeapSize
        while i > -1:
            Heap.min_heap(heap, i)                         
            i = i - 1
        return heap


    def min_heap(heap, i):
        n = len(heap)
        left = int(2 * i + 1)
        right = int(2 * i + 2)
        if left < n and heap[left] < heap[i]:
            min = left
        else:
            min = i    
        if right < n and heap[right] < heap[min]:
            min = right
        if min != i:
            temp = heap[i]
            Heap.swaps.append([i, min])
            heap[i] = heap[min]
            heap[min] = temp
            Heap.min_heap(heap, min)

    def print_swaps():
        print (len(Heap.swaps))
        for x in Heap.swaps:
            print(x[0],x[1])
    
def main():
    key = input()
    if key[0] == "F":
        fileName = input("Input file name:")
        fileName = "tests/" + filename
        f = open(fileName, "r")
        n = int(f.readline())
        data = list(map(int, f.readline().split()))
    
    elif key[0] == "I":
        n = int(input())
        data = list(map(int, input().split()))    
       
    assert len(data) == n

    Heap.build_heap(data, n)
    Heap.print_swaps()


if __name__ == "__main__":
    main()
