import numpy as np 

def function(x):

	i0 = x
	r2 = 1
	paths = []
	try:
		if x <= 5:
			i0 = r2/i0
			paths.append(1)
		else:
			x = x-x
			x = x*5
			r2 = r2-7
			paths.append(2)
		if r2 <= 6:
			r2 = r2-5
			x = x-1
			paths.append(3)
		else:
			i0 = r2/i0
			i0 = i0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))