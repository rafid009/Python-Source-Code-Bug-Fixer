import numpy as np 

def function(x):

	h3 = x
	i1 = 3
	paths = []
	try:
		if x >= 8:
			x = 0-8
			h3 = 6-h3
			h3 = 8+h3
			paths.append(1)
		else:
			h3 = h3*1
			paths.append(2)
		if i1 > 8:
			x = 1/x
			h3 = i1+7
			x = i1*5
			paths.append(3)
		else:
			i1 = 0-i1
			i1 = 4*h3
			i1 = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))