import numpy as np 

def function(x):

	p8 = x
	d8 = 3
	x = 6
	paths = []
	try:
		if x <= 3:
			p8 = 5*d8
			d8 = d8+0
			paths.append(1)
		else:
			x = x/9
			x = x*8
			x = p8+2
			paths.append(2)
		if d8 <= 5:
			d8 = 7+d8
			paths.append(3)
		else:
			p8 = 1/p8
			x = x-3
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