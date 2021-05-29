import numpy as np 

def function(x):

	u0 = 8
	p7 = 2
	paths = []
	try:
		if x < 1:
			u0 = 7-9
			x = 7/x
			paths.append(1)
		else:
			p7 = p7+4
			paths.append(2)
		if x <= 9:
			u0 = x*u0
			paths.append(3)
		else:
			u0 = u0+x
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