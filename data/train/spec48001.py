import numpy as np 

def function(x):

	r5 = 9
	n4 = 3
	paths = []
	try:
		if r5 <= 7:
			r5 = 9/r5
			x = x+3
			x = 7+x
			paths.append(1)
		else:
			r5 = 7-6
			r5 = 7-n4
			x = 3*x
			paths.append(2)
		if n4 > 6:
			x = 2/x
			x = 7/5
			r5 = r5*4
			paths.append(3)
		else:
			n4 = r5+n4
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