import numpy as np 

def function(x):

	h3 = 8
	h1 = 6
	x = x
	paths = []
	try:
		if h1 < 0:
			h1 = h1-4
			x = x/4
			paths.append(1)
		else:
			h1 = h1/2
			paths.append(2)
		if x > 2:
			x = x+3
			h1 = h1-5
			h1 = h1*9
			paths.append(3)
		else:
			h1 = h1*7
			h3 = x*h3
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h3 = h1**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))