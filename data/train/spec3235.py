import numpy as np 

def function(x):

	v8 = x
	d0 = x
	paths = []
	try:
		if x > 3:
			v8 = 4-v8
			d0 = d0+3
			x = 8*x
			paths.append(1)
		else:
			d0 = 9*d0
			x = d0*x
			paths.append(2)
		if v8 < 8:
			v8 = 7*v8
			x = d0/x
			paths.append(3)
		else:
			d0 = 7*d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))