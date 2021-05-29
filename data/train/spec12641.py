import numpy as np 

def function(x):

	f3 = x
	u5 = x
	x = x
	paths = []
	try:
		if f3 >= 9:
			f3 = x-x
			x = x-3
			paths.append(1)
		else:
			u5 = 4*u5
			u5 = u5/9
			x = 2*x
			paths.append(2)
		if x <= 4:
			x = 1-f3
			x = 0-6
			f3 = 2/f3
			paths.append(3)
		else:
			f3 = 6*f3
			x = 9/u5
			x = u5/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))