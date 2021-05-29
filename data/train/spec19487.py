import numpy as np 

def function(x):

	t9 = 1
	g2 = x
	paths = []
	try:
		if t9 <= 5:
			t9 = t9+3
			paths.append(1)
		else:
			g2 = g2-t9
			g2 = x-x
			t9 = t9-5
			paths.append(2)
		if x > 9:
			t9 = g2-t9
			g2 = 0/7
			t9 = 4-t9
			paths.append(3)
		else:
			g2 = g2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))