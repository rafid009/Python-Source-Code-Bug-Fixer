import numpy as np 

def function(x):

	t7 = x
	q0 = x
	paths = []
	try:
		if x < 0:
			q0 = 0/q0
			q0 = 1*q0
			t7 = q0-t7
			paths.append(1)
		else:
			x = 4/1
			q0 = x-6
			paths.append(2)
		if q0 < 3:
			t7 = t7-4
			paths.append(3)
		else:
			x = 8/x
			t7 = 4-t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))