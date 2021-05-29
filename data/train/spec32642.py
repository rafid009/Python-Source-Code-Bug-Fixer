import numpy as np 

def function(x):

	g9 = 4
	t8 = 2
	paths = []
	try:
		if t8 >= 4:
			g9 = t8+g9
			t8 = t8/6
			paths.append(1)
		else:
			t8 = t8-t8
			paths.append(2)
		if g9 > 4:
			g9 = g9+4
			paths.append(3)
		else:
			g9 = g9-0
			t8 = t8-2
			g9 = t8+1
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