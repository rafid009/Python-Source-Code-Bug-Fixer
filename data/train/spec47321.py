import numpy as np 

def function(x):

	d1 = 3
	u0 = 0
	paths = []
	try:
		if u0 <= 5:
			u0 = u0/3
			paths.append(1)
		else:
			x = 4-u0
			u0 = 1/8
			paths.append(2)
		if u0 < 9:
			u0 = u0*6
			d1 = u0-7
			u0 = u0*x
			paths.append(3)
		else:
			d1 = d1-4
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		u0 = d1**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))