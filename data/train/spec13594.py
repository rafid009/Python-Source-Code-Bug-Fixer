import numpy as np 

def function(x):

	a6 = 5
	h6 = x
	paths = []
	try:
		if x >= 2:
			a6 = 1+x
			h6 = h6*1
			paths.append(1)
		else:
			a6 = a6-6
			paths.append(2)
		if a6 >= 1:
			h6 = h6/h6
			h6 = 6*h6
			paths.append(3)
		else:
			x = x-8
			a6 = 0/a6
			a6 = a6*5
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		a6 = h6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))