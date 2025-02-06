#You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list
# of numbers as an agrument and returns only prime
# numbers from the list.

def filter_prime(nums):
    def is_prime(num):
        if num<2:
            return False
        for i in range (2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    return[num for num in nums if is_prime(num)]
print(filter_prime([1,2,3,4,5,67,8,9]))
                
    #output [2, 3, 5, 67]
    
    
    
    

        
        