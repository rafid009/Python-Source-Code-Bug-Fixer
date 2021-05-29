import numpy as np 

def function(x):

	g9 = x
	t0 = 7
	x = x
	paths = []
	try:
		if x >= 9:
			t0 = t0-7
			x = 2*x
			x = x+4
			paths.append(1)
		else:
			t0 = g9+t0
			paths.append(2)
		if t0 >= 6:
			x = 4/x
			t0 = t0/g9
			paths.append(3)
		else:
			t0 = 9*4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))