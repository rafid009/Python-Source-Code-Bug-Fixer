import numpy as np 

def function(x):

	d9 = x
	d7 = 0
	paths = []
	try:
		if x >= 1:
			d9 = 4+d7
			d7 = 5+d7
			d7 = 4-d9
			paths.append(1)
		else:
			d7 = d7+6
			x = x/4
			paths.append(2)
		if x < 3:
			d9 = x*d9
			paths.append(3)
		else:
			x = 8*d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))