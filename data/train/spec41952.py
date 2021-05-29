import numpy as np 

def function(x):

	h6 = x
	x2 = x
	paths = []
	try:
		if x > 8:
			x = x*4
			paths.append(1)
		else:
			x2 = x2/x2
			paths.append(2)
		if x2 >= 8:
			h6 = 7-h6
			x = 6+6
			x2 = x+x2
			paths.append(3)
		else:
			x2 = x2-6
			x2 = x+x2
			x2 = x2+h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))