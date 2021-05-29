import numpy as np 

def function(x):

	r0 = 2
	a4 = x
	paths = []
	try:
		if x >= 8:
			x = 6*x
			r0 = r0-4
			x = x-r0
			paths.append(1)
		else:
			x = x+r0
			paths.append(2)
		if a4 > 8:
			x = x-3
			x = a4/r0
			x = x*0
			paths.append(3)
		else:
			r0 = a4-r0
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))