import numpy as np 

def function(x):

	y4 = x
	t9 = 5
	paths = []
	try:
		if x > 6:
			y4 = y4-4
			t9 = t9/4
			paths.append(1)
		else:
			x = x/4
			x = y4+9
			x = x-7
			paths.append(2)
		if t9 >= 9:
			x = 1-x
			t9 = 0*y4
			t9 = 7-t9
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))