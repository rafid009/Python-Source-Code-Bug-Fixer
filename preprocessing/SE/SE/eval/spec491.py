import numpy as np 

def function(x):

	m6 = 6
	d0 = x
	x = x
	paths = []
	try:
		if x >= 4:
			x = 1-x
			paths.append(1)
		else:
			x = 8*d0
			x = x+6
			m6 = 7*2
			paths.append(2)
		if d0 < 4:
			x = x-0
			paths.append(3)
		else:
			d0 = 1/6
			x = d0*6
			d0 = d0/6
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