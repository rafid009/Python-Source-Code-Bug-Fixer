import numpy as np 

def function(x):

	r5 = 8
	n5 = x
	paths = []
	try:
		if n5 < 5:
			n5 = 3-n5
			x = 4*3
			x = x+8
			paths.append(1)
		else:
			n5 = n5-9
			x = 2*x
			x = 5/2
			paths.append(2)
		if x <= 8:
			r5 = x+6
			x = 9-5
			paths.append(3)
		else:
			x = 0*x
			n5 = 2-n5
			x = x-7
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