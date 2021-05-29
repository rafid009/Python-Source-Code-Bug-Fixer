import numpy as np 

def function(x):

	d2 = x
	b7 = 0
	paths = []
	try:
		if b7 < 4:
			d2 = d2-d2
			d2 = d2+x
			x = x+2
			paths.append(1)
		else:
			d2 = d2/d2
			paths.append(2)
		if b7 < 8:
			b7 = 6/6
			x = b7-6
			d2 = 3*7
			paths.append(3)
		else:
			b7 = 1-b7
			d2 = 0*b7
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