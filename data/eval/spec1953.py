import numpy as np 

def function(x):

	v8 = 3
	d0 = x
	paths = []
	try:
		if v8 < 3:
			d0 = 4+d0
			paths.append(1)
		else:
			d0 = d0+x
			d0 = v8+d0
			d0 = 2*d0
			paths.append(2)
		if x <= 9:
			v8 = 9*v8
			paths.append(3)
		else:
			x = x/8
			v8 = 1/v8
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