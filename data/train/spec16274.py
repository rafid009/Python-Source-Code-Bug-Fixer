import numpy as np 

def function(x):

	l0 = 7
	d4 = 0
	x = x
	paths = []
	try:
		if x > 3:
			x = x+2
			l0 = l0/l0
			d4 = 8+d4
			paths.append(1)
		else:
			l0 = l0+6
			paths.append(2)
		if l0 < 5:
			l0 = 5-d4
			x = l0*x
			x = x/8
			paths.append(3)
		else:
			l0 = 0-l0
			x = 3+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))