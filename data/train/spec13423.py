import numpy as np 

def function(x):

	t6 = 8
	z4 = x
	paths = []
	try:
		if t6 <= 2:
			t6 = 1-t6
			x = 1/z4
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x > 0:
			t6 = 8/t6
			paths.append(3)
		else:
			t6 = t6*7
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))