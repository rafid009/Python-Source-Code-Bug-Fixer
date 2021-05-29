import numpy as np 

def function(x):

	d4 = 8
	a8 = x
	paths = []
	try:
		if d4 >= 0:
			x = x+d4
			a8 = a8/d4
			a8 = 9-d4
			paths.append(1)
		else:
			a8 = a8*0
			paths.append(2)
		if d4 > 0:
			a8 = a8/6
			x = 4+x
			paths.append(3)
		else:
			x = x-8
			a8 = 9/x
			a8 = d4*a8
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