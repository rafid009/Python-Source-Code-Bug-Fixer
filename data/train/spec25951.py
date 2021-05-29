import numpy as np 

def function(x):

	v9 = 5
	d0 = x
	paths = []
	try:
		if x >= 2:
			d0 = d0-6
			paths.append(1)
		else:
			d0 = d0+3
			x = x*7
			v9 = v9*6
			paths.append(2)
		if v9 < 1:
			d0 = 8+d0
			v9 = v9/1
			x = x+x
			paths.append(3)
		else:
			v9 = 3/v9
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		v9 = d0**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))