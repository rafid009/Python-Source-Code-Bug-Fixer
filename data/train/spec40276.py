import numpy as np 

def function(x):

	a4 = 5
	y7 = 3
	x = x
	paths = []
	try:
		if a4 <= 5:
			a4 = 6-0
			x = x-3
			a4 = 4*a4
			paths.append(1)
		else:
			a4 = a4*7
			y7 = 0*2
			x = x-x
			paths.append(2)
		if a4 <= 5:
			a4 = 3+a4
			a4 = 1*a4
			paths.append(3)
		else:
			a4 = 3-x
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		y7 = a4**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))