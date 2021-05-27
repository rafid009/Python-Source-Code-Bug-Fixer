import numpy as np 

def function(x):

	r8 = x
	u6 = x
	paths = []
	try:
		if u6 <= 8:
			u6 = 5/u6
			paths.append(1)
		else:
			x = x-1
			x = x*6
			r8 = 9+x
			paths.append(2)
		if x > 5:
			r8 = x/r8
			paths.append(3)
		else:
			u6 = 9*u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))