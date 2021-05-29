import numpy as np 

def function(x):

	n0 = 1
	b6 = x
	paths = []
	try:
		if b6 <= 1:
			n0 = x*n0
			b6 = 1+0
			paths.append(1)
		else:
			n0 = x/x
			n0 = n0*5
			x = 5/x
			paths.append(2)
		if n0 < 8:
			b6 = b6/x
			x = x*x
			paths.append(3)
		else:
			n0 = b6/5
			b6 = b6*5
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		n0 = b6**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))