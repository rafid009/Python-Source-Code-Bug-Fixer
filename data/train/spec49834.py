import numpy as np 

def function(x):

	t8 = x
	g5 = 0
	paths = []
	try:
		if x >= 8:
			t8 = t8+6
			x = x-9
			paths.append(1)
		else:
			x = 5+4
			paths.append(2)
		if g5 > 7:
			t8 = x+4
			g5 = g5+0
			g5 = 9+g5
			paths.append(3)
		else:
			g5 = 4*g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))