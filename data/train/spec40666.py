import numpy as np 

def function(x):

	e1 = x
	h6 = 2
	paths = []
	try:
		if x > 1:
			e1 = e1*h6
			e1 = 3+3
			h6 = h6-8
			paths.append(1)
		else:
			x = x*e1
			paths.append(2)
		if x > 0:
			x = 0/8
			x = x-x
			paths.append(3)
		else:
			e1 = e1/3
			e1 = x/6
			e1 = h6*e1
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))