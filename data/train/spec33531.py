import numpy as np 

def function(x):

	y6 = 1
	t3 = 5
	paths = []
	try:
		if t3 >= 1:
			t3 = t3*9
			paths.append(1)
		else:
			x = x-x
			y6 = x/y6
			y6 = 6/y6
			paths.append(2)
		if t3 >= 1:
			t3 = x+4
			paths.append(3)
		else:
			x = x*6
			y6 = y6-0
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