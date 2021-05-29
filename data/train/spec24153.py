import numpy as np 

def function(x):

	x3 = x
	u5 = x
	paths = []
	try:
		if x3 <= 9:
			x = 5*x
			x3 = x3-x3
			paths.append(1)
		else:
			x3 = x+x
			u5 = u5-1
			x3 = 6*u5
			paths.append(2)
		if x <= 2:
			u5 = u5/x
			u5 = u5+1
			x3 = x/x
			paths.append(3)
		else:
			x = 7-x
			x3 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))