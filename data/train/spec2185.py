import numpy as np 

def function(x):

	d5 = 0
	v1 = x
	paths = []
	try:
		if x >= 3:
			d5 = 9*d5
			v1 = x*v1
			paths.append(1)
		else:
			d5 = 3/x
			paths.append(2)
		if d5 < 2:
			d5 = 4/x
			v1 = d5+9
			v1 = v1/9
			paths.append(3)
		else:
			d5 = 6+3
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