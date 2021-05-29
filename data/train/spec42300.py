import numpy as np 

def function(x):

	d8 = 7
	b2 = x
	paths = []
	try:
		if b2 < 2:
			b2 = b2/1
			paths.append(1)
		else:
			b2 = b2+b2
			d8 = 2*d8
			d8 = d8/8
			paths.append(2)
		if b2 <= 6:
			b2 = 1/1
			d8 = x-9
			d8 = 2*6
			paths.append(3)
		else:
			d8 = x-d8
			x = 2/8
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))