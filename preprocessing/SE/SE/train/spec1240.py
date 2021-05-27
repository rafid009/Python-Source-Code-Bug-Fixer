import numpy as np 

def function(x):

	a9 = x
	t9 = 9
	paths = []
	try:
		if t9 > 2:
			t9 = t9+4
			paths.append(1)
		else:
			t9 = a9*t9
			t9 = 2-t9
			a9 = x/3
			paths.append(2)
		if t9 >= 8:
			x = 7/x
			x = t9-x
			paths.append(3)
		else:
			a9 = a9*5
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