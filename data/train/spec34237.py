import numpy as np 

def function(x):

	y3 = x
	r4 = 5
	paths = []
	try:
		if r4 > 0:
			x = 6+x
			y3 = x*y3
			paths.append(1)
		else:
			y3 = 5*6
			r4 = 3/x
			x = 3+x
			paths.append(2)
		if y3 > 6:
			x = 9*x
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))