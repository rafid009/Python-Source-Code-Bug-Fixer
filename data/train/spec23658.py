import numpy as np 

def function(x):

	u2 = 1
	x7 = x
	x = x
	paths = []
	try:
		if u2 >= 3:
			x7 = 7/x7
			x7 = x7+2
			x = 6+1
			paths.append(1)
		else:
			x = 0-x
			u2 = 5/u2
			paths.append(2)
		if u2 >= 4:
			u2 = x7*7
			x = x/x
			paths.append(3)
		else:
			x = 2-1
			x = x*x
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))