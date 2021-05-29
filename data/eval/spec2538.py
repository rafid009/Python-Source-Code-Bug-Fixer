import numpy as np 

def function(x):

	t9 = x
	u5 = 7
	paths = []
	try:
		if t9 < 7:
			x = 3+x
			x = 3*x
			paths.append(1)
		else:
			x = 9-u5
			paths.append(2)
		if t9 < 0:
			u5 = 3/u5
			paths.append(3)
		else:
			x = t9*4
			t9 = t9-0
			u5 = x-2
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