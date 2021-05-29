import numpy as np 

def function(x):

	a9 = 5
	u6 = x
	paths = []
	try:
		if u6 < 3:
			a9 = a9-0
			a9 = 4-a9
			paths.append(1)
		else:
			u6 = u6*1
			paths.append(2)
		if u6 <= 1:
			a9 = u6*x
			u6 = 7*u6
			paths.append(3)
		else:
			x = x-3
			a9 = 4*1
			x = x-3
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