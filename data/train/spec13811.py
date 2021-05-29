import numpy as np 

def function(x):

	n8 = 3
	h8 = x
	paths = []
	try:
		if h8 < 8:
			h8 = 7*h8
			h8 = 6+x
			paths.append(1)
		else:
			n8 = n8*7
			x = n8/x
			x = 1-x
			paths.append(2)
		if n8 > 4:
			n8 = h8/9
			x = x/6
			paths.append(3)
		else:
			h8 = x/h8
			x = h8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))