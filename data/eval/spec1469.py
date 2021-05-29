import numpy as np 

def function(x):

	t6 = x
	u0 = 3
	paths = []
	try:
		if t6 > 7:
			x = x+6
			paths.append(1)
		else:
			u0 = 0/8
			paths.append(2)
		if x >= 8:
			u0 = u0-u0
			u0 = u0+2
			paths.append(3)
		else:
			u0 = 9/1
			u0 = u0-t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))