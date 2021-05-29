import numpy as np 

def function(x):

	t5 = x
	g7 = 8
	paths = []
	try:
		if x >= 3:
			t5 = t5-x
			paths.append(1)
		else:
			g7 = 0-t5
			paths.append(2)
		if x < 2:
			g7 = g7/g7
			t5 = t5-9
			x = x-7
			paths.append(3)
		else:
			g7 = 4/4
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))