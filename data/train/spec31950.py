import numpy as np 

def function(x):

	v0 = 5
	h1 = 8
	paths = []
	try:
		if h1 < 8:
			x = x-8
			paths.append(1)
		else:
			v0 = h1/4
			x = x/8
			v0 = h1-4
			paths.append(2)
		if h1 > 6:
			v0 = 2-v0
			v0 = 9/v0
			paths.append(3)
		else:
			v0 = 5/v0
			h1 = 2*x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))