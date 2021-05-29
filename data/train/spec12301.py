import numpy as np 

def function(x):

	r2 = x
	h4 = x
	paths = []
	try:
		if r2 < 2:
			x = x+h4
			x = 9/x
			paths.append(1)
		else:
			r2 = 1-r2
			paths.append(2)
		if x < 9:
			x = x-4
			x = x+x
			r2 = 0+r2
			paths.append(3)
		else:
			r2 = r2-h4
			r2 = 9+x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))