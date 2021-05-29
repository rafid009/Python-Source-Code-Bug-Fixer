import numpy as np 

def function(x):

	e6 = x
	f9 = 5
	paths = []
	try:
		if x < 3:
			x = f9*7
			paths.append(1)
		else:
			e6 = e6-f9
			e6 = e6-2
			e6 = 0+6
			paths.append(2)
		if f9 < 7:
			f9 = f9-x
			paths.append(3)
		else:
			x = 2/x
			x = 5-x
			e6 = 5+e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))