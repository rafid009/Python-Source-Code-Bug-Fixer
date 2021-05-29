import numpy as np 

def function(x):

	b6 = 0
	d4 = 2
	paths = []
	try:
		if b6 < 3:
			b6 = b6*3
			x = 9*x
			paths.append(1)
		else:
			x = b6*x
			b6 = x+b6
			x = d4-6
			paths.append(2)
		if d4 > 8:
			b6 = d4+x
			d4 = d4*8
			x = 5/x
			paths.append(3)
		else:
			x = 7-x
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