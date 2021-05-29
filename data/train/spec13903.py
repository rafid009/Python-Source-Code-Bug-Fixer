import numpy as np 

def function(x):

	d7 = x
	p1 = x
	paths = []
	try:
		if p1 < 8:
			d7 = d7*p1
			p1 = p1/8
			paths.append(1)
		else:
			d7 = p1-4
			paths.append(2)
		if x >= 2:
			x = 3/6
			paths.append(3)
		else:
			d7 = 0+d7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))