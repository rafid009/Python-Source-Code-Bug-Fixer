import numpy as np 

def function(x):

	r7 = 2
	n4 = 4
	paths = []
	try:
		if x > 4:
			r7 = 7/x
			r7 = 7-9
			paths.append(1)
		else:
			r7 = x*x
			x = x/8
			paths.append(2)
		if n4 >= 7:
			x = 0*x
			paths.append(3)
		else:
			x = x/2
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