import numpy as np 

def function(x):

	w4 = x
	t9 = 8
	paths = []
	try:
		if t9 <= 9:
			t9 = t9/x
			paths.append(1)
		else:
			x = 6/x
			w4 = t9-9
			x = x-w4
			paths.append(2)
		if t9 < 1:
			w4 = t9*x
			paths.append(3)
		else:
			t9 = t9/4
			x = x-2
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))