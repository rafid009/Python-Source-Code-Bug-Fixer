import numpy as np 

def function(x):

	u1 = x
	u6 = x
	paths = []
	try:
		if u1 >= 5:
			u1 = 0+u1
			u6 = 7-u6
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if u1 >= 6:
			u1 = u6/u6
			paths.append(3)
		else:
			u6 = 1/4
			x = 9-2
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