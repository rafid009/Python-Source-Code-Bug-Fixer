import numpy as np 

def function(x):

	y5 = x
	e6 = 0
	paths = []
	try:
		if e6 > 6:
			x = x-8
			y5 = 7-9
			x = 6/7
			paths.append(1)
		else:
			y5 = y5*1
			paths.append(2)
		if y5 > 7:
			x = x*6
			y5 = 5-3
			y5 = 5*y5
			paths.append(3)
		else:
			x = x/2
			e6 = 9+6
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		e6 = y5**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))