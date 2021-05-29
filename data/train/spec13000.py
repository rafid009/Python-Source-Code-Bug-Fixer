import numpy as np 

def function(x):

	u9 = 2
	v0 = 1
	paths = []
	try:
		if x > 5:
			x = x+4
			u9 = 8-u9
			v0 = v0*v0
			paths.append(1)
		else:
			u9 = 6*u9
			paths.append(2)
		if v0 <= 1:
			u9 = 0/3
			paths.append(3)
		else:
			x = v0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))