import numpy as np 

def function(x):

	a8 = 5
	r4 = 3
	paths = []
	try:
		if x > 4:
			a8 = 8*7
			paths.append(1)
		else:
			a8 = 9+a8
			r4 = r4*6
			paths.append(2)
		if a8 < 5:
			x = 1-x
			x = a8/r4
			paths.append(3)
		else:
			a8 = a8+2
			r4 = x+a8
			a8 = 4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))