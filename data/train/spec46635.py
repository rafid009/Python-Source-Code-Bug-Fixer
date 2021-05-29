import numpy as np 

def function(x):

	p4 = 8
	k5 = 8
	paths = []
	try:
		if x < 0:
			p4 = p4/p4
			paths.append(1)
		else:
			x = 8+k5
			paths.append(2)
		if p4 >= 4:
			p4 = p4+p4
			paths.append(3)
		else:
			p4 = 9+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))