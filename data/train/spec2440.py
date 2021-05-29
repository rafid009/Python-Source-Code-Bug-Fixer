import numpy as np 

def function(x):

	d5 = x
	v4 = x
	x = 2
	paths = []
	try:
		if d5 >= 9:
			v4 = v4/3
			v4 = 4-4
			d5 = d5/x
			paths.append(1)
		else:
			x = x*d5
			v4 = v4*v4
			paths.append(2)
		if d5 <= 9:
			x = x-d5
			paths.append(3)
		else:
			d5 = d5-x
			v4 = x+9
			x = 8-v4
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