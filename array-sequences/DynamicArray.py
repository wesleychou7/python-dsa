import ctypes

class DynamicArray(object):
    """
    Dynamic Array class
    """

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    
    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n


    def __getitem__(self, i):
        """
        Return element at index i
        """
        if not (0 <= i <= self.n):
            return IndexError("i is out of bounds.")
        
        return self.A[i]


    def append(self, element):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        self.A[self.n] = element
        self.n += 1


    def resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap)

        for i in range(self.n):
            B[i] = self.A[i]
        
        self.A = B
        self.capacity = new_cap


    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()



if __name__ == '__main__':
    
    arr = DynamicArray()
    arr.append("John")
    print(len(arr))
    print(arr[0])