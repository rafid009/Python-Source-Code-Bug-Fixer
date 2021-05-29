import numpy as np 

def function(x):

	r5 = 3
	n9 = 8
	paths = []
	try:
		if n9 <= 0:
			n9 = n9*x
			paths.append(1)
		else:
			r5 = n9-n9
			paths.append(2)
		if x < 7:
			n9 = 2/n9
			paths.append(3)
		else:
			r5 = n9*x
			r5 = 9+r5
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))