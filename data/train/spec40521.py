import numpy as np 

def function(x):

	n8 = x
	a7 = 6
	paths = []
	try:
		if a7 <= 2:
			n8 = n8+3
			x = 9*8
			n8 = 9+n8
			paths.append(1)
		else:
			a7 = a7+8
			x = 3/x
			paths.append(2)
		if a7 <= 4:
			n8 = 1+n8
			x = x*x
			a7 = a7+9
			paths.append(3)
		else:
			a7 = x*a7
			n8 = n8/8
			x = 7+a7
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