import numpy as np 

def function(x):

	d9 = 3
	d6 = x
	paths = []
	try:
		if x >= 1:
			x = x+8
			paths.append(1)
		else:
			x = x-4
			d6 = d6+6
			d6 = d6+0
			paths.append(2)
		if d9 < 9:
			d6 = d6*7
			d9 = d9*x
			d9 = 3+9
			paths.append(3)
		else:
			x = 4/x
			d6 = 5+9
			d6 = d6/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))