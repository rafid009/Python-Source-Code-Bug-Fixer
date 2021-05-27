import numpy as np 

def function(x):

	b9 = 9
	u0 = 7
	paths = []
	try:
		if u0 <= 3:
			x = x-3
			b9 = 1+u0
			paths.append(1)
		else:
			u0 = u0*7
			u0 = u0/8
			u0 = u0-x
			paths.append(2)
		if u0 < 3:
			u0 = 1*u0
			paths.append(3)
		else:
			u0 = u0/7
			x = 3-x
			b9 = u0-b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))