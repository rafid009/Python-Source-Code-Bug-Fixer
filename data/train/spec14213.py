import numpy as np 

def function(x):

	p8 = 4
	d4 = 8
	paths = []
	try:
		if x > 4:
			x = 3-4
			paths.append(1)
		else:
			d4 = d4+4
			paths.append(2)
		if p8 >= 0:
			d4 = 9-2
			p8 = 0*2
			paths.append(3)
		else:
			x = x/x
			x = 0/x
			x = x-1
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