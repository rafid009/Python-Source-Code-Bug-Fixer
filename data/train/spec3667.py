import numpy as np 

def function(x):

	n0 = 2
	l2 = 5
	paths = []
	try:
		if x > 5:
			n0 = n0+8
			n0 = n0*0
			l2 = n0/x
			paths.append(1)
		else:
			n0 = 2/x
			n0 = x*8
			paths.append(2)
		if l2 < 1:
			x = 3+9
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))