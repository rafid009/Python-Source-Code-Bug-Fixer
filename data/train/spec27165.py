import numpy as np 

def function(x):

	n1 = x
	j7 = 4
	paths = []
	try:
		if j7 < 5:
			x = 5*n1
			x = 1-x
			paths.append(1)
		else:
			x = 3-x
			x = 4+n1
			n1 = j7/n1
			paths.append(2)
		if j7 >= 5:
			n1 = n1-j7
			j7 = j7/9
			paths.append(3)
		else:
			j7 = 2/j7
			x = n1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))