import numpy as np 

def function(x):

	e1 = 8
	k5 = 0
	paths = []
	try:
		if x <= 3:
			e1 = k5/4
			paths.append(1)
		else:
			x = x*k5
			e1 = e1/2
			paths.append(2)
		if e1 >= 9:
			x = x/x
			k5 = 0-k5
			paths.append(3)
		else:
			k5 = 7+0
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