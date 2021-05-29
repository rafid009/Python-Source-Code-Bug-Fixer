import numpy as np 

def function(x):

	t8 = x
	g6 = x
	paths = []
	try:
		if x >= 9:
			t8 = t8/1
			x = x*9
			g6 = 0+g6
			paths.append(1)
		else:
			t8 = 0+g6
			paths.append(2)
		if x < 3:
			x = 1-x
			g6 = 4+3
			g6 = g6/8
			paths.append(3)
		else:
			t8 = 5+t8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))