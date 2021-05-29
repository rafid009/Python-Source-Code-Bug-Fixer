import numpy as np 

def function(x):

	e9 = 2
	u6 = 1
	paths = []
	try:
		if x <= 9:
			u6 = u6/7
			paths.append(1)
		else:
			e9 = x/6
			paths.append(2)
		if x >= 4:
			x = 2*x
			u6 = 5*1
			x = x*u6
			paths.append(3)
		else:
			x = x*5
			x = 6/x
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