import numpy as np 

def function(x):

	v1 = 9
	h7 = x
	paths = []
	try:
		if h7 >= 5:
			h7 = h7*5
			v1 = 2*v1
			v1 = v1*v1
			paths.append(1)
		else:
			h7 = v1/h7
			v1 = 6*v1
			paths.append(2)
		if h7 <= 5:
			h7 = h7-6
			paths.append(3)
		else:
			h7 = h7*3
			x = x+h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))