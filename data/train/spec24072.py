import numpy as np 

def function(x):

	r9 = x
	f9 = 0
	paths = []
	try:
		if r9 >= 2:
			f9 = f9*x
			r9 = r9/r9
			r9 = 4*r9
			paths.append(1)
		else:
			x = 6+r9
			paths.append(2)
		if r9 < 8:
			r9 = r9+f9
			x = x/5
			x = x*r9
			paths.append(3)
		else:
			r9 = 4-r9
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