import numpy as np 

def function(x):

	d4 = x
	p3 = x
	paths = []
	try:
		if d4 < 0:
			d4 = d4*5
			x = x*9
			paths.append(1)
		else:
			x = 9/x
			p3 = p3*7
			p3 = 6-p3
			paths.append(2)
		if p3 < 9:
			x = p3-x
			paths.append(3)
		else:
			x = 9-x
			p3 = 0-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))