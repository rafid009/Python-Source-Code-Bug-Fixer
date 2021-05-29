import numpy as np 

def function(x):

	j1 = 9
	n1 = x
	paths = []
	try:
		if x >= 4:
			j1 = j1+9
			j1 = 8/j1
			paths.append(1)
		else:
			j1 = 9-n1
			x = n1-x
			paths.append(2)
		if n1 >= 0:
			n1 = n1-3
			x = x*9
			n1 = j1+2
			paths.append(3)
		else:
			j1 = n1-x
			j1 = x*n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))