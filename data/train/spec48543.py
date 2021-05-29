import numpy as np 

def function(x):

	u5 = 7
	m9 = x
	paths = []
	try:
		if u5 < 1:
			x = 0*x
			u5 = m9-1
			paths.append(1)
		else:
			u5 = u5+4
			x = 4-x
			paths.append(2)
		if u5 >= 3:
			u5 = 2*u5
			u5 = x*6
			paths.append(3)
		else:
			x = x*u5
			x = 9*x
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