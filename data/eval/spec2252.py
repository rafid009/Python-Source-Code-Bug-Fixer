import numpy as np 

def function(x):

	h7 = 6
	e1 = 2
	paths = []
	try:
		if h7 >= 0:
			h7 = h7*x
			paths.append(1)
		else:
			e1 = e1*h7
			x = x/x
			x = x+h7
			paths.append(2)
		if h7 >= 1:
			e1 = 0*9
			x = x+3
			x = e1+8
			paths.append(3)
		else:
			e1 = e1*e1
			x = x-x
			e1 = h7+e1
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))