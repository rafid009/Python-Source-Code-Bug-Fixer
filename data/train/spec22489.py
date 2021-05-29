import numpy as np 

def function(x):

	h1 = x
	r7 = 6
	paths = []
	try:
		if h1 >= 1:
			x = h1+x
			x = 9-0
			x = x/r7
			paths.append(1)
		else:
			h1 = 9-6
			paths.append(2)
		if h1 >= 8:
			r7 = 0-r7
			paths.append(3)
		else:
			h1 = 2+h1
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))