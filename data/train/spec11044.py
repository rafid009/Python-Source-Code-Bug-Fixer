import numpy as np 

def function(x):

	y4 = x
	t9 = x
	x = x
	paths = []
	try:
		if x < 5:
			y4 = x-y4
			x = y4+y4
			paths.append(1)
		else:
			x = x-t9
			t9 = 8-x
			t9 = x*t9
			paths.append(2)
		if x >= 5:
			t9 = 1+t9
			x = 9/2
			paths.append(3)
		else:
			y4 = 0-5
			t9 = t9/y4
			t9 = 9/y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))