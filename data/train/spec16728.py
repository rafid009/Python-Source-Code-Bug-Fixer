import numpy as np 

def function(x):

	k4 = x
	d0 = x
	paths = []
	try:
		if d0 >= 7:
			k4 = k4-2
			k4 = 8-k4
			k4 = d0*9
			paths.append(1)
		else:
			x = x*3
			k4 = 5-3
			paths.append(2)
		if k4 >= 5:
			k4 = 2+k4
			d0 = d0+8
			paths.append(3)
		else:
			d0 = k4/x
			x = d0/9
			d0 = 7+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))