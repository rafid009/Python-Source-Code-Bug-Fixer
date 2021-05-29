import numpy as np 

def function(x):

	o4 = x
	u5 = x
	paths = []
	try:
		if x >= 2:
			u5 = u5+u5
			paths.append(1)
		else:
			u5 = o4*u5
			paths.append(2)
		if x < 5:
			x = o4*1
			u5 = 9*u5
			paths.append(3)
		else:
			u5 = u5+u5
			u5 = u5*u5
			x = x*x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))