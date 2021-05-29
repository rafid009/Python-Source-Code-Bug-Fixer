import numpy as np 

def function(x):

	l8 = x
	p4 = x
	paths = []
	try:
		if x > 4:
			p4 = 8/x
			p4 = p4/4
			x = x*7
			paths.append(1)
		else:
			l8 = 0+8
			l8 = x-l8
			paths.append(2)
		if x < 3:
			l8 = 5-x
			l8 = 1-7
			paths.append(3)
		else:
			p4 = p4*1
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