import numpy as np 

def function(x):

	t0 = x
	n8 = x
	paths = []
	try:
		if x <= 3:
			t0 = 6*x
			x = x*n8
			paths.append(1)
		else:
			t0 = 2*t0
			n8 = 5+n8
			x = 5*n8
			paths.append(2)
		if n8 >= 3:
			t0 = 0+t0
			paths.append(3)
		else:
			n8 = n8+0
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))