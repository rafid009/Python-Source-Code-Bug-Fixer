import numpy as np 

def function(x):

	p4 = x
	p2 = x
	x = 5
	paths = []
	try:
		if p2 <= 6:
			p4 = p4-0
			paths.append(1)
		else:
			p2 = 2-p4
			p4 = p2*p4
			paths.append(2)
		if x <= 6:
			p4 = p4*7
			paths.append(3)
		else:
			p4 = 5*x
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