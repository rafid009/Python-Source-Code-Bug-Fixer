import numpy as np 

def function(x):

	a6 = 1
	t7 = 3
	paths = []
	try:
		if x <= 4:
			t7 = 0-0
			t7 = 3*t7
			paths.append(1)
		else:
			t7 = 3-1
			paths.append(2)
		if a6 < 9:
			t7 = t7-x
			paths.append(3)
		else:
			a6 = 2*9
			t7 = t7/5
			x = t7+7
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