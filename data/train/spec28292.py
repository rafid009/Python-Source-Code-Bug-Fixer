import numpy as np 

def function(x):

	h1 = 8
	r1 = x
	paths = []
	try:
		if x >= 9:
			h1 = 0-h1
			h1 = 4-h1
			paths.append(1)
		else:
			x = x/5
			h1 = 9-0
			paths.append(2)
		if x < 9:
			r1 = r1-6
			r1 = r1/2
			x = x/x
			paths.append(3)
		else:
			x = 8*h1
			r1 = 0*5
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		h1 = r1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))