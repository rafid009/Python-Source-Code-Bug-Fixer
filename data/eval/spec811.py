import numpy as np 

def function(x):

	x5 = x
	e5 = x
	paths = []
	try:
		if x > 3:
			x = x5*7
			paths.append(1)
		else:
			x5 = x5/7
			e5 = e5-1
			paths.append(2)
		if x5 >= 5:
			x5 = x5-7
			paths.append(3)
		else:
			x5 = 4+x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))