import numpy as np 

def function(x):

	v5 = 6
	d1 = 2
	paths = []
	try:
		if x >= 0:
			v5 = v5+v5
			v5 = 4/v5
			paths.append(1)
		else:
			v5 = v5-6
			d1 = 0*d1
			paths.append(2)
		if d1 > 5:
			d1 = 9/d1
			v5 = v5/1
			paths.append(3)
		else:
			v5 = 3+9
			x = v5-x
			d1 = d1/v5
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