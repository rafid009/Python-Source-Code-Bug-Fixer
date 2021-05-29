import numpy as np 

def function(x):

	y7 = x
	t9 = 5
	paths = []
	try:
		if x <= 0:
			t9 = 1-t9
			x = 2*y7
			paths.append(1)
		else:
			t9 = t9/6
			y7 = y7/7
			paths.append(2)
		if y7 < 3:
			x = x-7
			x = 7+x
			t9 = 8+1
			paths.append(3)
		else:
			x = 5/9
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