import numpy as np 

def function(x):

	x1 = 8
	u3 = x
	paths = []
	try:
		if x > 8:
			x1 = 1-x1
			paths.append(1)
		else:
			x = u3+7
			x1 = x1*6
			x1 = x1/x1
			paths.append(2)
		if x1 > 5:
			x1 = u3*1
			paths.append(3)
		else:
			x = x1-x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x1 = u3**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))