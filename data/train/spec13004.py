import numpy as np 

def function(x):

	d2 = x
	l0 = 6
	x = 7
	paths = []
	try:
		if d2 >= 8:
			d2 = d2+l0
			d2 = x/6
			paths.append(1)
		else:
			d2 = 0+d2
			d2 = d2-6
			paths.append(2)
		if x >= 0:
			l0 = 3*l0
			x = x*d2
			paths.append(3)
		else:
			x = d2+x
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