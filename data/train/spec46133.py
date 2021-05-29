import numpy as np 

def function(x):

	t8 = x
	g8 = x
	paths = []
	try:
		if x < 8:
			g8 = 0+g8
			paths.append(1)
		else:
			g8 = g8-6
			paths.append(2)
		if x <= 1:
			t8 = t8+g8
			g8 = g8/4
			paths.append(3)
		else:
			t8 = 9*t8
			t8 = x+0
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