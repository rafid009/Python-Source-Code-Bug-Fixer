import numpy as np 

def function(x):

	u1 = 7
	l1 = x
	paths = []
	try:
		if x < 9:
			l1 = 1-x
			u1 = 8*9
			x = x*1
			paths.append(1)
		else:
			u1 = u1-5
			x = x-8
			paths.append(2)
		if x > 3:
			l1 = l1/l1
			u1 = 0/u1
			paths.append(3)
		else:
			x = 4-u1
			u1 = 5*x
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