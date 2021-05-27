import numpy as np 

def function(x):

	q8 = 2
	v0 = 9
	paths = []
	try:
		if q8 > 4:
			q8 = 7+5
			x = 9+x
			q8 = 7/8
			paths.append(1)
		else:
			x = 9*x
			x = x/5
			q8 = q8-4
			paths.append(2)
		if q8 < 2:
			v0 = 1/x
			q8 = q8*6
			paths.append(3)
		else:
			q8 = q8-5
			v0 = 0*0
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