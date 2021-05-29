import numpy as np 

def function(x):

	o4 = 5
	p9 = 7
	paths = []
	try:
		if o4 < 8:
			p9 = 0-6
			o4 = o4*7
			paths.append(1)
		else:
			x = 6/p9
			x = 3/x
			paths.append(2)
		if o4 >= 3:
			o4 = 6/7
			paths.append(3)
		else:
			x = 9/6
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