import numpy as np 

def function(x):

	a5 = 6
	r4 = 4
	x = x
	paths = []
	try:
		if x < 1:
			x = 9-x
			a5 = a5*2
			paths.append(1)
		else:
			a5 = a5/2
			x = 1-x
			paths.append(2)
		if r4 < 8:
			r4 = 4-r4
			a5 = 5*2
			paths.append(3)
		else:
			a5 = 7/5
			r4 = r4+8
			x = a5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))