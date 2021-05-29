import numpy as np 

def function(x):

	l0 = x
	d2 = x
	paths = []
	try:
		if x >= 7:
			l0 = l0/l0
			d2 = 0+d2
			paths.append(1)
		else:
			l0 = 5/l0
			x = 5/x
			paths.append(2)
		if x > 4:
			d2 = x-6
			d2 = 4*2
			paths.append(3)
		else:
			l0 = 0-0
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))