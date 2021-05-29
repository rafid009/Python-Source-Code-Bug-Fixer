import numpy as np 

def function(x):

	d7 = 9
	o1 = 3
	paths = []
	try:
		if x > 6:
			x = x*8
			x = x*8
			paths.append(1)
		else:
			d7 = d7+3
			o1 = 3-o1
			paths.append(2)
		if d7 < 0:
			x = d7*d7
			x = x*d7
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))