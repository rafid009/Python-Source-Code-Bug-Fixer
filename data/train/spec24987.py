import numpy as np 

def function(x):

	p4 = x
	k4 = 3
	paths = []
	try:
		if x < 8:
			x = x/k4
			paths.append(1)
		else:
			x = 4*6
			p4 = p4-5
			x = 4-3
			paths.append(2)
		if x >= 2:
			k4 = k4-8
			p4 = 7-p4
			paths.append(3)
		else:
			k4 = x+k4
			x = 3*x
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