import numpy as np 

def function(x):

	u9 = x
	n0 = x
	x = 4
	paths = []
	try:
		if n0 >= 7:
			n0 = 9*n0
			u9 = 4/u9
			paths.append(1)
		else:
			u9 = 3/u9
			paths.append(2)
		if u9 > 8:
			u9 = 1-n0
			paths.append(3)
		else:
			n0 = 2-n0
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))