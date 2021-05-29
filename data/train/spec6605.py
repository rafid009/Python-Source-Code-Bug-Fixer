import numpy as np 

def function(x):

	t4 = 6
	a0 = 4
	paths = []
	try:
		if x > 2:
			t4 = t4-7
			paths.append(1)
		else:
			a0 = a0+0
			a0 = a0-3
			paths.append(2)
		if x > 6:
			a0 = a0-8
			t4 = x-t4
			paths.append(3)
		else:
			t4 = 3/a0
			t4 = 5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))