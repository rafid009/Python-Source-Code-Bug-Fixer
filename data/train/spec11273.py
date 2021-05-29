import numpy as np 

def function(x):

	p4 = x
	n6 = 3
	x = x
	paths = []
	try:
		if n6 > 3:
			x = n6/7
			paths.append(1)
		else:
			n6 = 1+4
			paths.append(2)
		if p4 < 6:
			p4 = 4+4
			n6 = n6-4
			n6 = x/7
			paths.append(3)
		else:
			x = x*3
			p4 = x*7
			p4 = p4*x
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