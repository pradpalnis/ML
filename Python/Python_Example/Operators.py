# Examples of Identity operators 
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3] 
b3 = [1,2,3] 


print(a1 is not b1) 


print(a2 is b2) 

# Output is False, since lists are mutable. 
print(a3 is b3) 


# Examples of Membership operator 
x = 'Geeks for Geeks'
y = {3:'a',4:'b'} 


print('G' in x) 

print('geeks' not in x) 

print('Geeks' not in x) 

print(3 in y) 

print('b' in y) 
