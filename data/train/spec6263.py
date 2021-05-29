import numpy as np 

def function(x):

	e2 = 3
	u1 = 8
	paths = []
	try:
		if e2 < 3:
			u1 = u1/e2
			paths.append(1)
		else:
			x = 1*x
			e2 = 1*e2
			paths.append(2)
		if e2 <= 7:
			u1 = u1+x
			paths.append(3)
		else:
			x = 8/1
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