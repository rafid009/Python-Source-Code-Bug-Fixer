import numpy as np 

def function(x):

	u7 = 4
	x1 = 6
	x = x
	paths = []
	try:
		if x1 < 7:
			u7 = x1*u7
			x1 = x/x1
			x = u7-1
			paths.append(1)
		else:
			x1 = 2/7
			u7 = 6*u7
			paths.append(2)
		if x > 9:
			x1 = 4/x1
			x1 = x1/6
			paths.append(3)
		else:
			u7 = u7+3
			x1 = x+x1
			x = x1/x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))