import numpy as np 

def function(x):

	k2 = 8
	r8 = x
	x = x
	paths = []
	try:
		if r8 <= 6:
			r8 = r8-3
			paths.append(1)
		else:
			k2 = k2*x
			x = r8+x
			paths.append(2)
		if k2 > 6:
			k2 = k2-8
			k2 = k2/4
			paths.append(3)
		else:
			r8 = r8*x
			r8 = r8*5
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