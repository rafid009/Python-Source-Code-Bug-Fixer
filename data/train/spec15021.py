import numpy as np 

def function(x):

	y6 = 5
	t9 = x
	paths = []
	try:
		if x > 2:
			t9 = t9+y6
			x = 1+x
			paths.append(1)
		else:
			t9 = 7/t9
			t9 = 6-t9
			paths.append(2)
		if y6 >= 8:
			t9 = 8+t9
			t9 = 1*t9
			y6 = y6-y6
			paths.append(3)
		else:
			x = 5-2
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))