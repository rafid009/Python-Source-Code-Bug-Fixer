import numpy as np 

def function(x):

	r1 = x
	r2 = 0
	paths = []
	try:
		if r1 <= 3:
			x = x-5
			r2 = x/x
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if r1 > 1:
			r2 = r2*5
			paths.append(3)
		else:
			r2 = 5/r2
			r2 = 0+r2
			r1 = r2*2
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