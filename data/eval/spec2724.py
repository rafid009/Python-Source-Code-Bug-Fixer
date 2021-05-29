import numpy as np 

def function(x):

	o7 = 2
	h1 = 3
	paths = []
	try:
		if x <= 7:
			o7 = 6+o7
			o7 = o7-0
			h1 = 2/h1
			paths.append(1)
		else:
			o7 = h1/h1
			o7 = 4*7
			x = x/2
			paths.append(2)
		if h1 >= 0:
			o7 = x*3
			paths.append(3)
		else:
			o7 = o7-5
			o7 = 7+4
			h1 = o7+x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		h1 = o7**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))