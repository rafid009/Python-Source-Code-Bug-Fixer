import numpy as np 

def function(x):

	f2 = 3
	r5 = x
	paths = []
	try:
		if x > 9:
			f2 = x-6
			x = 2*x
			x = 1+4
			paths.append(1)
		else:
			x = 9-1
			r5 = 6/r5
			f2 = 6-2
			paths.append(2)
		if r5 < 7:
			x = x-x
			x = x-4
			paths.append(3)
		else:
			f2 = f2-6
			x = x+0
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