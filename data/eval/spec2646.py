import numpy as np 

def function(x):

	d6 = x
	a8 = 4
	paths = []
	try:
		if x <= 9:
			a8 = 7/a8
			paths.append(1)
		else:
			a8 = a8+d6
			a8 = 6+6
			x = x+8
			paths.append(2)
		if a8 <= 7:
			x = x*7
			x = 0-x
			paths.append(3)
		else:
			x = x+x
			d6 = a8-2
			x = x/d6
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