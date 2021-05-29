import numpy as np 

def function(x):

	u0 = x
	x3 = x
	paths = []
	try:
		if u0 >= 4:
			x3 = 9/6
			u0 = u0/7
			paths.append(1)
		else:
			u0 = 2+x
			x = x/6
			paths.append(2)
		if x < 8:
			u0 = u0-4
			x3 = 7*x3
			u0 = u0+x
			paths.append(3)
		else:
			u0 = u0*x3
			u0 = u0/6
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))