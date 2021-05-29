import numpy as np 

def function(x):

	e4 = x
	t4 = 5
	paths = []
	try:
		if e4 < 5:
			t4 = t4/e4
			e4 = 8*e4
			paths.append(1)
		else:
			e4 = 6/8
			e4 = 9*e4
			t4 = e4/2
			paths.append(2)
		if e4 < 1:
			t4 = 3*3
			paths.append(3)
		else:
			x = x/9
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