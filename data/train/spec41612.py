import numpy as np 

def function(x):

	t4 = 1
	y0 = 6
	paths = []
	try:
		if x < 7:
			t4 = 0+x
			y0 = 0-y0
			paths.append(1)
		else:
			t4 = t4/4
			t4 = t4-9
			y0 = y0/6
			paths.append(2)
		if t4 >= 2:
			y0 = y0*y0
			t4 = y0/7
			paths.append(3)
		else:
			t4 = 8*t4
			t4 = t4/x
			y0 = 8/y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		t4 = y0**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))