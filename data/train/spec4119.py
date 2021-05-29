import numpy as np 

def function(x):

	y2 = 4
	t9 = x
	paths = []
	try:
		if y2 < 1:
			t9 = t9*t9
			paths.append(1)
		else:
			t9 = 5+t9
			paths.append(2)
		if x >= 1:
			y2 = 8/2
			paths.append(3)
		else:
			t9 = t9/y2
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))