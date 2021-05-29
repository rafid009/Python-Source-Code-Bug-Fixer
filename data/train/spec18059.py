import numpy as np 

def function(x):

	e4 = x
	p6 = 8
	paths = []
	try:
		if p6 < 2:
			e4 = 3*p6
			e4 = 8-1
			x = x-0
			paths.append(1)
		else:
			e4 = e4*3
			p6 = 3*p6
			paths.append(2)
		if p6 < 2:
			x = 6/x
			x = p6/4
			paths.append(3)
		else:
			p6 = 7/p6
			e4 = e4/9
			e4 = e4*1
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))