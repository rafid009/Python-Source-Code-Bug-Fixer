import numpy as np 

def function(x):

	x9 = x
	l1 = 2
	paths = []
	try:
		if x <= 1:
			x = 9+6
			paths.append(1)
		else:
			l1 = 4+l1
			x = x*1
			paths.append(2)
		if l1 > 2:
			x = x9*x9
			paths.append(3)
		else:
			x9 = x9+l1
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))