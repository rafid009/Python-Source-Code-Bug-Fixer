import numpy as np 

def function(x):

	v6 = x
	u1 = 4
	paths = []
	try:
		if v6 > 7:
			x = 7*x
			x = x+0
			paths.append(1)
		else:
			u1 = u1-x
			v6 = v6-4
			x = 5-x
			paths.append(2)
		if v6 < 5:
			x = x/v6
			v6 = 9-u1
			paths.append(3)
		else:
			u1 = 1-4
			u1 = 9+u1
			x = x+u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))