import numpy as np 

def function(x):

	a6 = 0
	z6 = x
	paths = []
	try:
		if z6 > 4:
			a6 = a6/z6
			paths.append(1)
		else:
			x = x/7
			x = 3-x
			paths.append(2)
		if x < 0:
			x = x-z6
			a6 = 3-0
			paths.append(3)
		else:
			x = 0/3
			a6 = a6-9
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))