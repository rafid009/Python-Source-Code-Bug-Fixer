import numpy as np 

def function(x):

	t7 = 3
	t9 = x
	paths = []
	try:
		if x >= 1:
			t9 = t9-x
			paths.append(1)
		else:
			t7 = t7/t9
			t9 = x/2
			t9 = 2-t9
			paths.append(2)
		if x <= 1:
			x = 7+x
			t7 = t7*6
			t7 = t7/t9
			paths.append(3)
		else:
			t7 = t9*9
			x = x-1
			x = 0/x
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