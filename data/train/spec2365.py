import numpy as np 

def function(x):

	l8 = 2
	t6 = 0
	paths = []
	try:
		if t6 > 6:
			t6 = x+l8
			paths.append(1)
		else:
			t6 = 2/8
			paths.append(2)
		if x > 1:
			t6 = l8+l8
			paths.append(3)
		else:
			t6 = t6+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))