import numpy as np 

def function(x):

	d8 = 7
	x5 = x
	paths = []
	try:
		if x5 <= 2:
			x = x-4
			d8 = 5/x5
			d8 = 0/x
			paths.append(1)
		else:
			x5 = x5+3
			paths.append(2)
		if d8 <= 1:
			x5 = d8+d8
			x = x*9
			paths.append(3)
		else:
			x = x+x5
			x = x*3
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