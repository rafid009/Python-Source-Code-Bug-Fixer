import numpy as np 

def function(x):

	x6 = x
	h4 = 3
	paths = []
	try:
		if h4 <= 1:
			x6 = x6+1
			paths.append(1)
		else:
			h4 = h4+3
			paths.append(2)
		if x6 >= 5:
			h4 = 4*3
			x = x-8
			x6 = 5+x6
			paths.append(3)
		else:
			x6 = x6+2
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