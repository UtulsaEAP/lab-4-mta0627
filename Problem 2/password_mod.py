"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Mason Anderson
Lab Time: 2/16/24 3:54 PM
"""

def password_mod():
    word = input()
    # Type your code here.
    password = word.replace('i','1').replace('a','@').replace('m','M').replace('B','8').replace('s','$') + '!'
    print(password)

if __name__ == "__main__":
    password_mod()