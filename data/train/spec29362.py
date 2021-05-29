import numpy as np 

def function(x):

	e8 = x
	d0 = 3
	paths = []
	try:
		if x > 0:
			e8 = e8/9
			paths.append(1)
		else:
			x = 4/x
			x = 8+0
			e8 = e8/9
			paths.append(2)
		if d0 < 4:
			d0 = d0+d0
			d0 = d0*e8
			paths.append(3)
		else:
			x = 6*6
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))