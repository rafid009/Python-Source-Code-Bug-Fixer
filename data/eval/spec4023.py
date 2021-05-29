import numpy as np 

def function(x):

	r3 = x
	h1 = x
	paths = []
	try:
		if h1 >= 3:
			h1 = h1-4
			paths.append(1)
		else:
			x = 2+6
			r3 = r3/x
			x = x+9
			paths.append(2)
		if x > 6:
			h1 = h1-0
			h1 = x/x
			paths.append(3)
		else:
			x = x-x
			x = 7*4
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		h1 = r3**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))