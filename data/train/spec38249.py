import numpy as np 

def function(x):

	u7 = x
	m0 = 2
	paths = []
	try:
		if m0 >= 7:
			x = x/x
			paths.append(1)
		else:
			u7 = u7+1
			u7 = u7/3
			x = x-u7
			paths.append(2)
		if m0 < 6:
			u7 = x/u7
			u7 = u7/7
			paths.append(3)
		else:
			x = x+7
			x = u7*x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))