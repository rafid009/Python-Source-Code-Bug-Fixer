import numpy as np 

def function(x):

	e6 = x
	p4 = x
	paths = []
	try:
		if x <= 6:
			p4 = 5+e6
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if e6 < 8:
			p4 = x/p4
			paths.append(3)
		else:
			p4 = 0*p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))