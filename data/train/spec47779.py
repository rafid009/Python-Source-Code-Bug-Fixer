import numpy as np 

def function(x):

	h3 = 9
	e6 = 7
	paths = []
	try:
		if x >= 2:
			h3 = h3+1
			e6 = e6-8
			paths.append(1)
		else:
			x = x/5
			h3 = h3+3
			x = e6/x
			paths.append(2)
		if h3 >= 7:
			h3 = h3/h3
			paths.append(3)
		else:
			x = h3-0
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))