import numpy as np 

def function(x):

	v5 = 2
	d4 = x
	paths = []
	try:
		if x <= 4:
			v5 = v5*v5
			d4 = v5*d4
			paths.append(1)
		else:
			x = x/v5
			x = 2*x
			x = 9+x
			paths.append(2)
		if x <= 3:
			v5 = 4*3
			x = v5/x
			paths.append(3)
		else:
			d4 = 9-d4
			v5 = d4+d4
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))