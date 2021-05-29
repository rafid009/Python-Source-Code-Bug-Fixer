import numpy as np 

def function(x):

	a4 = x
	x8 = x
	paths = []
	try:
		if x > 3:
			x8 = x8*1
			paths.append(1)
		else:
			a4 = a4/6
			paths.append(2)
		if x8 > 5:
			a4 = 1*a4
			a4 = a4*x8
			paths.append(3)
		else:
			x8 = x8-3
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))