import numpy as np 

def function(x):

	r9 = 1
	b8 = 5
	paths = []
	try:
		if r9 < 2:
			r9 = b8-r9
			r9 = x/2
			b8 = 6+6
			paths.append(1)
		else:
			x = b8/6
			paths.append(2)
		if r9 <= 7:
			x = 6/x
			paths.append(3)
		else:
			r9 = r9*x
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