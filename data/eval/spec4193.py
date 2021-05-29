import numpy as np 

def function(x):

	p6 = 7
	d0 = x
	paths = []
	try:
		if p6 < 1:
			p6 = 9/p6
			paths.append(1)
		else:
			d0 = 5-d0
			p6 = p6*p6
			paths.append(2)
		if x <= 0:
			x = 3-p6
			paths.append(3)
		else:
			d0 = 8/p6
			p6 = 3*x
			d0 = d0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))