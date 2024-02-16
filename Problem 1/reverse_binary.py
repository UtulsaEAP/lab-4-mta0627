"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Mason Anderson
Lab Time: 2/16/24 3:40 PM

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    
    x = user_num
    start = True
    
    while x > 0:
        
        digit = x % 2
        x //= 2    
        
        if start == True:
            binary_num = str(digit)
            start = False
        else:
            binary_num = binary_num + str(digit) 

    print (binary_num)

    

if __name__ == "__main__":
    reverse_binary()