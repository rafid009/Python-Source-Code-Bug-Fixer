import numpy as np 

def function(x):

	x1 = x
	u0 = 5
	paths = []
	try:
		if x > 0:
			u0 = 9*u0
			paths.append(1)
		else:
			x = u0+x1
			paths.append(2)
		if u0 < 3:
			x = x-0
			u0 = 4/2
			paths.append(3)
		else:
			u0 = u0/u0
			x = u0+5
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