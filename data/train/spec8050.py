import numpy as np 

def function(x):

	t7 = 9
	x4 = x
	paths = []
	try:
		if t7 >= 1:
			x = 3*x
			paths.append(1)
		else:
			t7 = t7/3
			paths.append(2)
		if t7 < 3:
			x4 = 9-x4
			t7 = t7*8
			paths.append(3)
		else:
			x = 5*6
			t7 = t7/6
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))