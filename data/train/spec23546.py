import numpy as np 

def function(x):

	j1 = 8
	u1 = 7
	paths = []
	try:
		if j1 <= 7:
			x = 1-x
			j1 = 0*u1
			paths.append(1)
		else:
			u1 = u1-1
			j1 = j1+u1
			u1 = u1/x
			paths.append(2)
		if u1 > 4:
			x = x-x
			paths.append(3)
		else:
			u1 = 2/u1
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