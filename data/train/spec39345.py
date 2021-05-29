import numpy as np 

def function(x):

	i1 = 9
	u6 = 7
	paths = []
	try:
		if i1 >= 8:
			i1 = 9/7
			i1 = x-8
			paths.append(1)
		else:
			u6 = 2-u6
			i1 = 1/x
			i1 = 0+0
			paths.append(2)
		if i1 >= 7:
			x = 0-x
			x = 1+u6
			paths.append(3)
		else:
			x = u6/x
			u6 = 5*u6
			i1 = i1/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))