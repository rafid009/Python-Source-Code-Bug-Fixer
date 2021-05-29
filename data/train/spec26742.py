import numpy as np 

def function(x):

	g8 = 8
	t0 = x
	paths = []
	try:
		if x <= 5:
			t0 = 5-t0
			t0 = t0-2
			t0 = 3*t0
			paths.append(1)
		else:
			x = x-g8
			g8 = 3/t0
			g8 = 1*g8
			paths.append(2)
		if g8 < 0:
			t0 = t0-t0
			t0 = g8-x
			paths.append(3)
		else:
			x = 5*x
			t0 = t0/6
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