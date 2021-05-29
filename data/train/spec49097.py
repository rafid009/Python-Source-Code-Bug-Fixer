import numpy as np 

def function(x):

	v7 = 8
	u0 = 2
	paths = []
	try:
		if x < 5:
			u0 = x-u0
			paths.append(1)
		else:
			u0 = u0+u0
			x = x*2
			paths.append(2)
		if u0 >= 7:
			x = 4-7
			x = 0/x
			paths.append(3)
		else:
			u0 = u0-v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))