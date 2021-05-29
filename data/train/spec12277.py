import numpy as np 

def function(x):

	r1 = x
	r5 = 1
	paths = []
	try:
		if r5 > 6:
			x = x-5
			paths.append(1)
		else:
			r5 = r1/r1
			paths.append(2)
		if x >= 1:
			r5 = r5+3
			r1 = 6/4
			x = r5-r5
			paths.append(3)
		else:
			r5 = r1*3
			x = x*9
			r5 = 7*x
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