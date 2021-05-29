import numpy as np 

def function(x):

	r5 = x
	f3 = 0
	paths = []
	try:
		if x >= 4:
			f3 = f3/4
			r5 = r5-f3
			f3 = f3/r5
			paths.append(1)
		else:
			x = x+5
			r5 = 1+f3
			paths.append(2)
		if x < 4:
			r5 = r5+r5
			paths.append(3)
		else:
			r5 = 2*f3
			f3 = x-f3
			r5 = f3-r5
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