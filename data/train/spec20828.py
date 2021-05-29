import numpy as np 

def function(x):

	r1 = 9
	o1 = x
	paths = []
	try:
		if x <= 5:
			r1 = r1+o1
			r1 = x/r1
			paths.append(1)
		else:
			x = r1*x
			o1 = o1-1
			paths.append(2)
		if r1 <= 6:
			x = 6*x
			o1 = r1*7
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))