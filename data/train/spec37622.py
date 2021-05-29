import numpy as np 

def function(x):

	x2 = x
	x1 = 6
	paths = []
	try:
		if x2 >= 4:
			x = x+0
			x = x*5
			paths.append(1)
		else:
			x = 0-x2
			paths.append(2)
		if x1 >= 9:
			x2 = 5/x2
			x = 2+9
			paths.append(3)
		else:
			x2 = x2/x1
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))