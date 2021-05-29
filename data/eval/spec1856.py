import numpy as np 

def function(x):

	v4 = x
	d0 = 1
	paths = []
	try:
		if v4 <= 1:
			d0 = d0-6
			d0 = d0/2
			d0 = 7/1
			paths.append(1)
		else:
			v4 = v4-6
			x = 9-d0
			paths.append(2)
		if v4 > 9:
			v4 = x/3
			paths.append(3)
		else:
			v4 = 9*2
			d0 = 6+d0
			x = x/8
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