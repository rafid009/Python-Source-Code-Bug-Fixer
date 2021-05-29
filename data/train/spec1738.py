import numpy as np 

def function(x):

	p4 = 3
	x1 = 3
	paths = []
	try:
		if x >= 2:
			p4 = x1-p4
			x = x*9
			paths.append(1)
		else:
			p4 = p4+x
			paths.append(2)
		if x1 > 6:
			x1 = 0-x1
			x1 = 4-x1
			paths.append(3)
		else:
			x1 = x1-7
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))