import numpy as np 

def function(x):

	n0 = x
	t9 = x
	paths = []
	try:
		if t9 < 6:
			n0 = 0-n0
			x = t9/x
			x = x+4
			paths.append(1)
		else:
			n0 = 2*n0
			x = 5*2
			paths.append(2)
		if n0 < 8:
			x = x+1
			n0 = 6/x
			t9 = t9/6
			paths.append(3)
		else:
			n0 = x/t9
			n0 = x*n0
			n0 = 2-n0
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