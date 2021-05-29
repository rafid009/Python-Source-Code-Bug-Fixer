import numpy as np 

def function(x):

	r3 = 4
	d4 = 1
	paths = []
	try:
		if x <= 9:
			x = 6+d4
			d4 = d4*x
			r3 = r3/x
			paths.append(1)
		else:
			x = 2+x
			r3 = 4-4
			d4 = d4/3
			paths.append(2)
		if x >= 0:
			d4 = d4-4
			r3 = 0-5
			paths.append(3)
		else:
			x = 1-5
			x = 2+x
			d4 = d4-x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))