import numpy as np 

def function(x):

	n1 = 4
	s7 = x
	x = 1
	paths = []
	try:
		if n1 >= 0:
			x = 2*x
			x = n1/9
			paths.append(1)
		else:
			n1 = n1-0
			x = x+0
			n1 = x-3
			paths.append(2)
		if n1 >= 9:
			s7 = 0-8
			paths.append(3)
		else:
			n1 = 4+n1
			x = x/s7
			x = x-1
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))