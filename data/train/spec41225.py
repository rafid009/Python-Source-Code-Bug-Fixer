import numpy as np 

def function(x):

	d0 = x
	v5 = 9
	paths = []
	try:
		if d0 < 8:
			v5 = v5+6
			paths.append(1)
		else:
			v5 = 3/v5
			v5 = v5+6
			paths.append(2)
		if x <= 8:
			x = x-4
			d0 = d0*7
			paths.append(3)
		else:
			d0 = 6+d0
			x = 7/6
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		v5 = d0**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))