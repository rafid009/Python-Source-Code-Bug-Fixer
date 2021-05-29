import numpy as np 

def function(x):

	g8 = x
	t0 = 7
	paths = []
	try:
		if t0 < 0:
			t0 = t0*g8
			t0 = t0+6
			paths.append(1)
		else:
			x = 8-1
			t0 = t0*x
			t0 = t0*1
			paths.append(2)
		if x >= 5:
			g8 = g8*7
			g8 = g8+t0
			t0 = 2/t0
			paths.append(3)
		else:
			x = 3/x
			t0 = t0*t0
			t0 = 4*6
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		t0 = g8**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))