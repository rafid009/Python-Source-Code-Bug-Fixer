import numpy as np 

def function(x):

	x8 = 1
	r5 = x
	paths = []
	try:
		if r5 <= 5:
			x8 = 4-x8
			paths.append(1)
		else:
			x8 = x8*r5
			paths.append(2)
		if x8 <= 2:
			x = x-7
			x = x-8
			r5 = r5*9
			paths.append(3)
		else:
			x8 = 4*x8
			r5 = r5*4
			x8 = 5/r5
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