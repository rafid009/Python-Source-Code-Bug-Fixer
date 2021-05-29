import numpy as np 

def function(x):

	j0 = 1
	d4 = 7
	paths = []
	try:
		if j0 <= 9:
			j0 = x+2
			j0 = x*x
			x = 1/x
			paths.append(1)
		else:
			d4 = d4-8
			d4 = 9*d4
			paths.append(2)
		if x <= 0:
			d4 = x+9
			paths.append(3)
		else:
			d4 = j0+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))