import numpy as np 

def function(x):

	e5 = 8
	u5 = 5
	paths = []
	try:
		if u5 < 7:
			e5 = e5/1
			paths.append(1)
		else:
			u5 = 3*8
			x = x/4
			paths.append(2)
		if x < 2:
			e5 = e5+8
			e5 = e5/x
			paths.append(3)
		else:
			x = x-2
			x = 6-e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))