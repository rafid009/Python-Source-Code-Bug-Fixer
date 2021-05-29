import numpy as np 

def function(x):

	p4 = x
	l8 = 6
	paths = []
	try:
		if p4 >= 2:
			x = x-x
			x = x/6
			p4 = x-p4
			paths.append(1)
		else:
			l8 = l8*5
			x = x/6
			x = l8*p4
			paths.append(2)
		if l8 >= 1:
			l8 = p4*9
			paths.append(3)
		else:
			p4 = 6/9
			x = 4-2
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