import numpy as np 

def function(x):

	p4 = 2
	d1 = x
	paths = []
	try:
		if p4 < 7:
			x = x*3
			x = 9-x
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if p4 < 3:
			p4 = x+3
			paths.append(3)
		else:
			p4 = 7-p4
			p4 = 9+p4
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