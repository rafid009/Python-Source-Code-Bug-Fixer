import numpy as np 

def function(x):

	e4 = x
	u3 = 9
	paths = []
	try:
		if e4 >= 4:
			u3 = e4-u3
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if u3 >= 8:
			x = x-3
			x = 4/6
			paths.append(3)
		else:
			e4 = e4/8
			e4 = x/8
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))