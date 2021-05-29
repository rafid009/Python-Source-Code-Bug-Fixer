import numpy as np 

def function(x):

	j1 = x
	n4 = 6
	paths = []
	try:
		if n4 < 8:
			n4 = n4*1
			n4 = n4+3
			j1 = 9+j1
			paths.append(1)
		else:
			j1 = 9/j1
			paths.append(2)
		if x < 3:
			j1 = 4/j1
			paths.append(3)
		else:
			n4 = j1*n4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		n4 = j1**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))