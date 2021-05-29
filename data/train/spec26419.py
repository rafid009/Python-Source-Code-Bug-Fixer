import numpy as np 

def function(x):

	n0 = 9
	t9 = x
	paths = []
	try:
		if n0 >= 1:
			x = x+6
			t9 = 7*t9
			paths.append(1)
		else:
			n0 = n0*7
			n0 = n0-x
			paths.append(2)
		if x <= 4:
			t9 = 1/t9
			t9 = t9*8
			t9 = x*2
			paths.append(3)
		else:
			n0 = t9/2
			x = 6/6
			n0 = 1-n0
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