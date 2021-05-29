import numpy as np 

def function(x):

	t9 = x
	u1 = 2
	paths = []
	try:
		if t9 > 8:
			x = t9/t9
			u1 = u1-3
			paths.append(1)
		else:
			u1 = x/2
			paths.append(2)
		if x <= 0:
			u1 = 1+6
			x = x/1
			paths.append(3)
		else:
			u1 = u1-7
			u1 = u1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))