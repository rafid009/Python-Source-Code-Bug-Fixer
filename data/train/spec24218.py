import numpy as np 

def function(x):

	a9 = 4
	u6 = x
	paths = []
	try:
		if x >= 2:
			x = x+a9
			paths.append(1)
		else:
			u6 = u6*8
			paths.append(2)
		if x >= 6:
			a9 = a9/1
			paths.append(3)
		else:
			a9 = 0*a9
			a9 = u6+a9
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))