import numpy as np 

def function(x):

	u1 = 5
	v8 = 6
	paths = []
	try:
		if v8 <= 7:
			x = 2*u1
			v8 = v8*u1
			paths.append(1)
		else:
			x = v8-x
			x = 0/x
			v8 = 9+u1
			paths.append(2)
		if v8 <= 1:
			x = x*8
			u1 = v8-u1
			paths.append(3)
		else:
			x = 4-x
			u1 = 6-u1
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