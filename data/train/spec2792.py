import numpy as np 

def function(x):

	i5 = x
	u4 = 2
	paths = []
	try:
		if i5 >= 0:
			i5 = x/i5
			paths.append(1)
		else:
			x = 6*x
			u4 = 6*u4
			u4 = 6-i5
			paths.append(2)
		if i5 >= 6:
			u4 = u4/2
			paths.append(3)
		else:
			i5 = 8-x
			u4 = x/u4
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))