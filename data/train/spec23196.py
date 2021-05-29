import numpy as np 

def function(x):

	r5 = 2
	x2 = 6
	paths = []
	try:
		if x <= 7:
			r5 = 9/7
			x = x/x2
			paths.append(1)
		else:
			r5 = r5+3
			x2 = x2*5
			x = 4*x
			paths.append(2)
		if x < 1:
			r5 = 7+9
			paths.append(3)
		else:
			r5 = 6*5
			r5 = 3/r5
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