class heap:
    def __init__(self):
        self.heap = []
        self.heap_curr_size = len(self.heap)


    def size(self):
        return self.heap_curr_size


    def is_empty(self):
        if (self.size() == 0):
            return True
        else:
            return False


    def __str__(self):
        return f"Heap: {self.heap}"

    def insert(self, key):
        self.heap.append(key)
        self.heap_curr_size += 1
        self.heapify_up(self.heap_curr_size -1)

    def heapify_up(self, index):
        while(index > 0):
            parent = (index -1)//2

            if(self.heap[index] < self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
        

    def heapify_down(self, index):
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        smallest_child = index

        if(left_child < self.heap_curr_size and self.heap[left_child] < self.heap[smallest_child]):
            smallest_child = left_child

        if(right_child < self.heap_curr_size and self.heap[right_child] < self.heap[smallest_child]):
            smallest_child = right_child
    
        if(smallest_child != index):
            self.heap[index], self.heap[smallest_child] = self.heap[smallest_child], self.heap[index]

            self.heapify_down(smallest_child)

    def peak(self):
        if self.heap_curr_size == 0:
            return None
        else:
            return self.heap[0]
    
    def decrease_key(self, index, new_key):
        if (new_key > self.heap[index]):
            return None
    
        self.heap[index] = new_key
        self.heapify_up(index)

    def extract_min(self):
        root = self.heap[0]
        last_element =  self.heap.pop()
        self.heap_curr_size -= 1

        if self.heap_curr_size > 0: 
            self.heap[0] = last_element
            self.heapify_down(0)
        return root

    def delete(self, index):
        self.decrease_key(index, float('-inf'))
        self.extract_min()

    def build_heap(self, array):
        self.heap = list(array)
        self.heap_curr_size = len(self.heap)
        starting_index = (self.heap_curr_size //2) -1

        for i in range(starting_index, -1, -1):
            self.heapify_down(i)


def heap_sort(array):
    heap1 = heap()
    heap1.build_heap(array)

    sorted_heap = []
    while heap1.size() > 0:
        sorted_heap.append(heap1.extract_min())
    return sorted_heap

def main():
    print("test 1:")
    test_heap = heap()
    nums1 = [15,10,20,8,25,3]
    for n in nums1:
        test_heap.insert(n)
        print(test_heap)

    print("test 2:")
    for i in range(3):
        curr_value = test_heap.extract_min()
        print("Extracted value:")
        print(curr_value)
        print(test_heap)
    
    print("test 3:")
    b_heap = heap()
    data = [42, 18, 7, 35, 12, 50, 3, 27]
    b_heap.build_heap(data)
    print(b_heap)

    print("test 4:")
    b_heap.decrease_key(5,1)
    print(b_heap)
    b_heap.delete(2)
    print(b_heap)

    print("test 5:")
    last_data = [64, 34, 25, 12, 22, 11]
    print(heap_sort(last_data))
    
if __name__ == "__main__":
    main()