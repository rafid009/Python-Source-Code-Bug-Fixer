import numpy as np 

def function(x):

	t9 = x
	y2 = 3
	paths = []
	try:
		if y2 > 0:
			x = 5-1
			t9 = t9-7
			x = x+t9
			paths.append(1)
		else:
			t9 = t9*7
			t9 = t9/8
			y2 = 1*4
			paths.append(2)
		if x <= 3:
			t9 = x*7
			x = t9/3
			x = x-t9
			paths.append(3)
		else:
			y2 = 5/7
			y2 = y2-1
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))