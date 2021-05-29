import numpy as np 

def function(x):

	v1 = x
	h1 = 1
	paths = []
	try:
		if x < 9:
			v1 = 2*h1
			paths.append(1)
		else:
			v1 = 6-1
			h1 = 6-3
			paths.append(2)
		if h1 < 1:
			h1 = 7-h1
			paths.append(3)
		else:
			h1 = 8+h1
			v1 = v1-x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))