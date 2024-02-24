"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Mason Anderson
Lab Time: 2/16/24 4:10 PM
"""

def inc_5():
    # Write your code here
    num1 = int(input())
    num2 = int(input())

    x = num1

    if num2 >= num1:
        
        while num2 >= x:
            print (f'{x}', end=' ')
            x += 5

    else:
        print ("Second integer can't be less than the first.")
        


if __name__ == '__main__':
    inc_5()