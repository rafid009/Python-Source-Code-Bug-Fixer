import numpy as np 

def function(x):

	e4 = x
	u3 = x
	paths = []
	try:
		if e4 >= 9:
			u3 = u3-9
			paths.append(1)
		else:
			x = x*x
			x = u3/7
			x = 8/x
			paths.append(2)
		if x >= 0:
			e4 = 7*5
			u3 = 6+e4
			paths.append(3)
		else:
			x = 7-x
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