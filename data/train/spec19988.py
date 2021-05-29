import numpy as np 

def function(x):

	j2 = x
	u9 = x
	x = x
	paths = []
	try:
		if x >= 7:
			u9 = u9*u9
			x = 9*6
			u9 = u9*u9
			paths.append(1)
		else:
			x = 3*u9
			paths.append(2)
		if x >= 2:
			u9 = u9/4
			x = 2/x
			paths.append(3)
		else:
			x = 6+x
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