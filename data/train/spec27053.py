import numpy as np 

def function(x):

	t4 = x
	t9 = 8
	paths = []
	try:
		if x > 0:
			x = x-t9
			paths.append(1)
		else:
			t4 = 6-t4
			t9 = t9-6
			x = t9*x
			paths.append(2)
		if x <= 1:
			t9 = t9+t9
			paths.append(3)
		else:
			x = x-7
			t9 = t9-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))