import numpy as np 

def function(x):

	n9 = 3
	t0 = x
	paths = []
	try:
		if x > 4:
			x = 7+x
			n9 = n9/t0
			x = 0+x
			paths.append(1)
		else:
			t0 = t0+6
			t0 = 3+t0
			paths.append(2)
		if t0 > 0:
			t0 = 9-t0
			paths.append(3)
		else:
			x = 4*x
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