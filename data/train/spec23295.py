import numpy as np 

def function(x):

	y5 = 5
	a3 = x
	paths = []
	try:
		if y5 <= 6:
			y5 = y5+0
			y5 = 8*y5
			a3 = a3*1
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if y5 <= 2:
			a3 = x-a3
			paths.append(3)
		else:
			a3 = a3+2
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))