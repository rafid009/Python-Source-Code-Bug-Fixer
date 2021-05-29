import numpy as np 

def function(x):

	t0 = 3
	n2 = 2
	paths = []
	try:
		if n2 > 9:
			t0 = 1*4
			x = t0*x
			paths.append(1)
		else:
			t0 = t0*8
			n2 = n2+3
			t0 = t0/x
			paths.append(2)
		if x > 2:
			n2 = 4-n2
			x = x-4
			paths.append(3)
		else:
			t0 = 2*t0
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))