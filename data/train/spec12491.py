import numpy as np 

def function(x):

	h1 = 3
	r1 = x
	paths = []
	try:
		if r1 < 4:
			x = 3/r1
			h1 = h1+h1
			x = x+7
			paths.append(1)
		else:
			r1 = r1+3
			paths.append(2)
		if h1 <= 7:
			x = 1/3
			x = r1/x
			x = x/6
			paths.append(3)
		else:
			r1 = 9+r1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))