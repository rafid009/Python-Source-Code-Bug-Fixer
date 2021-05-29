import numpy as np 

def function(x):

	n4 = 1
	j1 = 7
	paths = []
	try:
		if n4 > 9:
			x = x-2
			paths.append(1)
		else:
			j1 = 2*j1
			n4 = n4*n4
			x = x+0
			paths.append(2)
		if n4 < 5:
			j1 = j1+1
			paths.append(3)
		else:
			j1 = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))