import numpy as np 

def function(x):

	r0 = x
	u6 = 2
	paths = []
	try:
		if x < 3:
			x = u6-x
			x = x*5
			r0 = 8*u6
			paths.append(1)
		else:
			r0 = 3+r0
			x = x*u6
			paths.append(2)
		if u6 > 6:
			x = 8*7
			r0 = r0-u6
			paths.append(3)
		else:
			r0 = 9+4
			r0 = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))