import numpy as np 

def function(x):

	l0 = x
	d2 = x
	paths = []
	try:
		if x > 4:
			x = x-4
			d2 = 4-2
			x = 5*8
			paths.append(1)
		else:
			l0 = l0/1
			l0 = l0*8
			x = 7+x
			paths.append(2)
		if d2 < 0:
			d2 = 4*d2
			paths.append(3)
		else:
			l0 = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))