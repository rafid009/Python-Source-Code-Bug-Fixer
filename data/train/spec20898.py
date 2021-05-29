import numpy as np 

def function(x):

	t7 = x
	z4 = x
	paths = []
	try:
		if x <= 1:
			t7 = t7*1
			paths.append(1)
		else:
			t7 = t7-0
			paths.append(2)
		if z4 >= 9:
			t7 = t7+4
			paths.append(3)
		else:
			x = t7-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))