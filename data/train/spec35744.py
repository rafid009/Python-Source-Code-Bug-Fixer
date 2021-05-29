import numpy as np 

def function(x):

	x2 = x
	d2 = x
	paths = []
	try:
		if x2 > 8:
			x = 9+x
			paths.append(1)
		else:
			d2 = 2-d2
			d2 = 1/3
			paths.append(2)
		if x2 < 6:
			d2 = d2-6
			x = d2+3
			x = d2*x
			paths.append(3)
		else:
			d2 = d2*4
			x = x+d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))