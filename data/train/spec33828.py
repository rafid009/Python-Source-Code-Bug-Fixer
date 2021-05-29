import numpy as np 

def function(x):

	t4 = x
	x1 = 6
	paths = []
	try:
		if t4 < 0:
			x = x+2
			paths.append(1)
		else:
			t4 = 9-x1
			x1 = 3/t4
			paths.append(2)
		if t4 > 4:
			x = 7-x
			t4 = 7-x1
			paths.append(3)
		else:
			x1 = x1-x
			x = x+1
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