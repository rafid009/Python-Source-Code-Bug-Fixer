import numpy as np 

def function(x):

	l9 = x
	t0 = 9
	paths = []
	try:
		if t0 <= 3:
			x = t0/2
			paths.append(1)
		else:
			l9 = 4/l9
			paths.append(2)
		if x >= 8:
			l9 = l9+l9
			x = 4-x
			x = l9/8
			paths.append(3)
		else:
			t0 = 1-t0
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