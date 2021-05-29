import numpy as np 

def function(x):

	t9 = x
	t1 = 2
	paths = []
	try:
		if x > 3:
			x = 4-t1
			t9 = t9/x
			t9 = 6*x
			paths.append(1)
		else:
			t1 = 3*t1
			paths.append(2)
		if x >= 2:
			t1 = x+t9
			t1 = 8/t1
			paths.append(3)
		else:
			t9 = 7*t9
			t9 = t1-t9
			t9 = t9*1
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