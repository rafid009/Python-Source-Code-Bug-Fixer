import numpy as np 

def function(x):

	q0 = x
	d0 = 7
	paths = []
	try:
		if x > 2:
			x = 7+4
			x = 2/9
			paths.append(1)
		else:
			q0 = q0/2
			d0 = d0/4
			paths.append(2)
		if x >= 0:
			x = x/4
			x = x/2
			q0 = q0-8
			paths.append(3)
		else:
			d0 = 8+6
			d0 = 4*2
			d0 = d0+x
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