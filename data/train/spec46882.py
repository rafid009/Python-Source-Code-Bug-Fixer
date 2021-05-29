import numpy as np 

def function(x):

	g6 = x
	t0 = x
	paths = []
	try:
		if x >= 9:
			g6 = g6+4
			paths.append(1)
		else:
			t0 = 7+6
			t0 = x+g6
			x = g6-5
			paths.append(2)
		if t0 <= 8:
			x = 0+t0
			paths.append(3)
		else:
			g6 = g6*2
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		t0 = g6**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))