import numpy as np 

def function(x):

	p4 = x
	n0 = 9
	paths = []
	try:
		if n0 >= 4:
			p4 = x+n0
			x = x+p4
			paths.append(1)
		else:
			x = 3-x
			x = n0+p4
			paths.append(2)
		if p4 >= 0:
			n0 = n0-x
			p4 = p4+5
			p4 = 1+n0
			paths.append(3)
		else:
			x = 5*5
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))