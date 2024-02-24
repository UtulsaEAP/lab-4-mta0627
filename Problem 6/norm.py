"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Mason Anderson
Lab Time: 8:02 PM 2/23/24
"""

def norm():
    # Write your code here
    
    num_of_data_values = int(input())
    for i in range(num_of_data_values):
        
        if i == 0:
            data_set = [float(input())]
        else:
            data_set.append(float(input()))
    
    max_value = max(data_set)
    adjusted_set = [num / max_value for num in data_set]
    
    for num in iter(adjusted_set):
        print (f'{num:.2f}')

if __name__ == "__main__":
    norm()