import numpy as np 

def function(x):

	b5 = 4
	d1 = x
	paths = []
	try:
		if d1 < 6:
			d1 = d1/d1
			paths.append(1)
		else:
			b5 = d1+3
			paths.append(2)
		if d1 < 4:
			x = 3+x
			paths.append(3)
		else:
			b5 = b5-2
			d1 = d1*3
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))