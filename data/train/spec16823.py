import numpy as np 

def function(x):

	v1 = x
	d6 = 5
	paths = []
	try:
		if v1 > 2:
			d6 = x-v1
			v1 = 3/4
			paths.append(1)
		else:
			v1 = v1*5
			d6 = 5/v1
			paths.append(2)
		if v1 < 3:
			x = x-2
			paths.append(3)
		else:
			x = x/5
			x = x-3
			v1 = v1*5
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