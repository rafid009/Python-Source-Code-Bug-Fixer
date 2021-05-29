import numpy as np 

def function(x):

	t9 = x
	r5 = 9
	x = x
	paths = []
	try:
		if x >= 2:
			x = t9*1
			t9 = t9/r5
			paths.append(1)
		else:
			t9 = 2-x
			paths.append(2)
		if x > 2:
			t9 = r5-r5
			paths.append(3)
		else:
			t9 = t9-4
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