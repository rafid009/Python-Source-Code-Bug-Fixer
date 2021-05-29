import numpy as np 

def function(x):

	q4 = 4
	h3 = 2
	x = x
	paths = []
	try:
		if h3 >= 3:
			x = 4-q4
			h3 = h3*2
			q4 = 0/q4
			paths.append(1)
		else:
			x = x*9
			h3 = 5*h3
			h3 = h3+q4
			paths.append(2)
		if h3 >= 6:
			x = x+x
			paths.append(3)
		else:
			x = 0/6
			h3 = h3/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))