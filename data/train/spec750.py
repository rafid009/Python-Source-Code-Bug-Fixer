import numpy as np 

def function(x):

	p7 = 6
	d8 = 2
	paths = []
	try:
		if p7 > 8:
			p7 = 7-d8
			x = 5-2
			paths.append(1)
		else:
			x = x-3
			p7 = d8/p7
			d8 = d8*9
			paths.append(2)
		if p7 > 4:
			d8 = 4*7
			d8 = d8*p7
			paths.append(3)
		else:
			x = x+2
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