import numpy as np 

def function(x):

	d0 = x
	e9 = 3
	paths = []
	try:
		if d0 >= 5:
			d0 = 1/d0
			e9 = 9+0
			paths.append(1)
		else:
			e9 = x+e9
			d0 = d0*6
			x = 0-7
			paths.append(2)
		if d0 <= 6:
			d0 = e9*7
			paths.append(3)
		else:
			d0 = 0/d0
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		d0 = e9**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))