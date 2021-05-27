import numpy as np 

def function(x):

	a3 = 4
	y3 = 7
	x = 4
	paths = []
	try:
		if y3 < 2:
			x = x*y3
			a3 = 6/7
			paths.append(1)
		else:
			a3 = 2-9
			a3 = a3*y3
			paths.append(2)
		if a3 > 5:
			x = 2*x
			paths.append(3)
		else:
			x = x-4
			y3 = x*y3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		y3 = a3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))