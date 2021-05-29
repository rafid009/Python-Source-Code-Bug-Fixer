import numpy as np 

def function(x):

	r9 = 4
	e8 = 2
	paths = []
	try:
		if r9 > 6:
			x = x-x
			x = 1*3
			r9 = 0+r9
			paths.append(1)
		else:
			r9 = 7*r9
			paths.append(2)
		if x >= 4:
			r9 = 9+r9
			x = x+7
			paths.append(3)
		else:
			x = x*8
			r9 = r9/8
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