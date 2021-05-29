import numpy as np 

def function(x):

	y0 = x
	t2 = x
	paths = []
	try:
		if y0 < 9:
			x = x-x
			x = 2-x
			y0 = 9-y0
			paths.append(1)
		else:
			t2 = t2/6
			paths.append(2)
		if x < 9:
			x = x-9
			t2 = 5/t2
			t2 = y0-t2
			paths.append(3)
		else:
			y0 = y0/3
			y0 = x+0
			y0 = 8/y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))