import numpy as np 

def function(x):

	g6 = 5
	t0 = x
	x = 1
	paths = []
	try:
		if g6 <= 2:
			x = x/t0
			paths.append(1)
		else:
			x = 3/6
			g6 = g6/5
			paths.append(2)
		if x < 8:
			x = x/9
			paths.append(3)
		else:
			t0 = 5-0
			t0 = t0-g6
			g6 = g6*g6
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))