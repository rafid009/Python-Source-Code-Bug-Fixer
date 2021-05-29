import numpy as np 

def function(x):

	g5 = x
	t0 = x
	paths = []
	try:
		if g5 > 1:
			x = x*t0
			t0 = t0-3
			t0 = g5*t0
			paths.append(1)
		else:
			g5 = g5+x
			t0 = 6*t0
			paths.append(2)
		if x < 9:
			x = 4+x
			x = 4/x
			t0 = x-6
			paths.append(3)
		else:
			g5 = 6-g5
			t0 = 0/t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))