import numpy as np 

def function(x):

	h6 = 7
	n5 = x
	paths = []
	try:
		if n5 > 7:
			x = 6+2
			paths.append(1)
		else:
			h6 = x*h6
			paths.append(2)
		if x <= 1:
			h6 = h6-3
			n5 = 5+n5
			n5 = n5*9
			paths.append(3)
		else:
			x = 0+8
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))