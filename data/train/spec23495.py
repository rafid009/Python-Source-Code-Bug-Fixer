import numpy as np 

def function(x):

	d8 = 6
	x2 = 4
	paths = []
	try:
		if x2 <= 9:
			x = 9-x
			x2 = x2+x
			x = x+x
			paths.append(1)
		else:
			x2 = x2+6
			paths.append(2)
		if x2 > 2:
			x2 = 0+x2
			x2 = x2*5
			d8 = d8+8
			paths.append(3)
		else:
			x2 = 5-x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))