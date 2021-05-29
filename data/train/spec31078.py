import numpy as np 

def function(x):

	t0 = x
	n7 = 7
	paths = []
	try:
		if n7 < 8:
			t0 = 7-t0
			x = 9+x
			paths.append(1)
		else:
			t0 = 4-t0
			x = n7+1
			x = t0+x
			paths.append(2)
		if x >= 7:
			x = x/7
			x = n7-x
			t0 = 3+5
			paths.append(3)
		else:
			n7 = n7+5
			x = n7-2
			n7 = x*n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))