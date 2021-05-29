import numpy as np 

def function(x):

	x3 = x
	r9 = 8
	x = x
	paths = []
	try:
		if x3 >= 6:
			x = 0+x3
			r9 = x-2
			r9 = 9/6
			paths.append(1)
		else:
			x3 = x*4
			x3 = r9+5
			x = x+0
			paths.append(2)
		if r9 >= 3:
			r9 = 4-3
			x = x+4
			paths.append(3)
		else:
			x3 = 9/x3
			x3 = r9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))