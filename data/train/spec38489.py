import numpy as np 

def function(x):

	y5 = 8
	t9 = 6
	paths = []
	try:
		if t9 >= 4:
			t9 = 3/t9
			paths.append(1)
		else:
			x = 7/x
			t9 = 3/6
			x = 9+x
			paths.append(2)
		if x <= 3:
			t9 = t9+5
			y5 = t9-9
			x = 5-y5
			paths.append(3)
		else:
			t9 = t9*x
			t9 = y5/3
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		t9 = y5**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))