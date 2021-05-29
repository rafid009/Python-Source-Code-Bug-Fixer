import numpy as np 

def function(x):

	d9 = 9
	p6 = 7
	paths = []
	try:
		if p6 < 2:
			p6 = p6*3
			p6 = p6*9
			paths.append(1)
		else:
			d9 = d9+8
			paths.append(2)
		if x < 1:
			p6 = d9*1
			paths.append(3)
		else:
			x = d9/1
			p6 = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))