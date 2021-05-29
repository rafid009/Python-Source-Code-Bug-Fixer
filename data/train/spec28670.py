import numpy as np 

def function(x):

	u0 = x
	a2 = 2
	paths = []
	try:
		if u0 < 0:
			x = x/a2
			paths.append(1)
		else:
			u0 = a2+4
			paths.append(2)
		if a2 > 0:
			u0 = u0*1
			a2 = 8/a2
			paths.append(3)
		else:
			a2 = u0*u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		a2 = u0**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))