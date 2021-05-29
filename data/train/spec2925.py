import numpy as np 

def function(x):

	d4 = x
	p8 = x
	paths = []
	try:
		if p8 > 0:
			p8 = p8/2
			d4 = 2-5
			x = 8-x
			paths.append(1)
		else:
			d4 = 2-d4
			paths.append(2)
		if x > 6:
			d4 = 5*d4
			d4 = 7*8
			p8 = p8*p8
			paths.append(3)
		else:
			d4 = 2*d4
			d4 = d4/d4
			d4 = x+d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))