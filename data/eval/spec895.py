import numpy as np 

def function(x):

	a6 = x
	x1 = x
	paths = []
	try:
		if a6 >= 4:
			x1 = 0-x1
			paths.append(1)
		else:
			a6 = x*2
			paths.append(2)
		if a6 < 3:
			x1 = 5/a6
			x = 7/2
			x = x/x
			paths.append(3)
		else:
			x = 0*8
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