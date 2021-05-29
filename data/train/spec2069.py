import numpy as np 

def function(x):

	n2 = 8
	h4 = x
	paths = []
	try:
		if h4 <= 7:
			x = x/6
			paths.append(1)
		else:
			h4 = 1+3
			paths.append(2)
		if n2 < 8:
			n2 = 1-h4
			x = h4-x
			paths.append(3)
		else:
			n2 = 7+h4
			h4 = h4*9
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))