import numpy as np 

def function(x):

	e9 = x
	r5 = x
	paths = []
	try:
		if x > 4:
			r5 = 0+6
			x = x*5
			paths.append(1)
		else:
			r5 = x/2
			r5 = r5/5
			paths.append(2)
		if x > 9:
			x = x/r5
			r5 = 4-r5
			paths.append(3)
		else:
			x = x-2
			e9 = x*9
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