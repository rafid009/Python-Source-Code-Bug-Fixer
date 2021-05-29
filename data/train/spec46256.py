import numpy as np 

def function(x):

	t5 = x
	n0 = x
	paths = []
	try:
		if n0 < 0:
			t5 = n0+x
			paths.append(1)
		else:
			x = x*9
			n0 = 8*n0
			paths.append(2)
		if n0 > 9:
			n0 = n0*t5
			n0 = n0-7
			paths.append(3)
		else:
			x = x+6
			n0 = t5-4
			n0 = n0/2
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))