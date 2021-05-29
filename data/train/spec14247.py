import numpy as np 

def function(x):

	a5 = x
	u0 = x
	paths = []
	try:
		if u0 < 5:
			u0 = u0*u0
			x = u0-1
			paths.append(1)
		else:
			x = x+7
			x = 1-u0
			x = 0*u0
			paths.append(2)
		if u0 <= 3:
			u0 = 7+5
			u0 = u0*x
			u0 = u0+9
			paths.append(3)
		else:
			u0 = u0+5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		u0 = a5**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))