"""
Complete the following python code to reverse the string entered by the user.

Name: Mason Anderson
Lab Time: 2/16/24
"""

def reverse_string():
    # YOUR CODE HERE
    
    string = 'start'
    iterations = 0
    
    while string != 'Done' and string != 'done' and string != 'd':
        string = input()
        iterations += 1
        
        if string != 'Done' and string != 'done' and string != 'd':
            
            for index, char in enumerate(string):
                if index == 0:
                    temp_string = char
                else:
                    temp_string = char + temp_string
            
            if iterations == 1:
                reverse_string = temp_string
            else:
                reverse_string = reverse_string + '\n' + temp_string
            
    print (reverse_string)
            
if __name__ == "__main__":
    reverse_string()