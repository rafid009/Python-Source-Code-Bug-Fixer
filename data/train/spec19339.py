import numpy as np 

def function(x):

	p6 = x
	x5 = 4
	paths = []
	try:
		if x5 > 8:
			x = x-x5
			x = 3+x
			paths.append(1)
		else:
			p6 = 4-p6
			x5 = 9-2
			x5 = p6+x5
			paths.append(2)
		if x >= 3:
			x5 = 8*3
			x5 = x5*3
			x5 = x/x5
			paths.append(3)
		else:
			x = x+x5
			x = 1/x5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x5 = p6**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))