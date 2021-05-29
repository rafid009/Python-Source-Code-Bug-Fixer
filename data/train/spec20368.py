import numpy as np 

def function(x):

	k4 = 7
	p7 = x
	x = 2
	paths = []
	try:
		if k4 > 6:
			x = x/k4
			x = 0/x
			k4 = k4/9
			paths.append(1)
		else:
			p7 = p7+2
			p7 = x-p7
			paths.append(2)
		if x >= 1:
			p7 = p7-p7
			paths.append(3)
		else:
			x = 1-3
			p7 = k4-p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))