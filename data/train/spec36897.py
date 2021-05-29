import numpy as np 

def function(x):

	a0 = 6
	y6 = 2
	paths = []
	try:
		if x <= 3:
			a0 = 9+a0
			paths.append(1)
		else:
			a0 = a0-x
			paths.append(2)
		if a0 > 9:
			y6 = y6+1
			x = 9+9
			y6 = 1/a0
			paths.append(3)
		else:
			x = x*a0
			y6 = 8/6
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))