import numpy as np 

def function(x):

	p0 = 0
	d8 = x
	paths = []
	try:
		if d8 >= 2:
			p0 = 2-p0
			paths.append(1)
		else:
			p0 = p0-7
			d8 = 7/d8
			p0 = d8/p0
			paths.append(2)
		if p0 < 3:
			p0 = 7/1
			paths.append(3)
		else:
			d8 = d8/5
			p0 = p0*1
			d8 = d8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))