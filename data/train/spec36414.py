import numpy as np 

def function(x):

	r1 = x
	n9 = 2
	paths = []
	try:
		if r1 > 7:
			r1 = 7/6
			paths.append(1)
		else:
			n9 = n9+6
			n9 = 9/n9
			paths.append(2)
		if x <= 1:
			x = x/n9
			x = 1*x
			paths.append(3)
		else:
			x = 9/8
			r1 = 3*n9
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