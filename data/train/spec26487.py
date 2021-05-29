import numpy as np 

def function(x):

	u4 = 7
	a7 = 3
	paths = []
	try:
		if a7 < 8:
			x = 5*x
			u4 = u4*u4
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if x <= 1:
			u4 = u4*5
			paths.append(3)
		else:
			x = 7*x
			a7 = a7-5
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))