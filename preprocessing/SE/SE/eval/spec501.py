import numpy as np 

def function(x):

	y0 = 2
	t6 = x
	x = 8
	paths = []
	try:
		if y0 < 9:
			y0 = y0/9
			paths.append(1)
		else:
			x = x-2
			x = 8+t6
			t6 = t6-5
			paths.append(2)
		if t6 >= 8:
			t6 = 5-6
			paths.append(3)
		else:
			t6 = 1*t6
			y0 = 1-7
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		t6 = y0**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))