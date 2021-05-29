import numpy as np 

def function(x):

	k5 = 6
	n0 = x
	paths = []
	try:
		if n0 <= 5:
			x = k5/x
			paths.append(1)
		else:
			n0 = 6*n0
			k5 = 2-k5
			paths.append(2)
		if n0 < 8:
			x = x+1
			n0 = n0/6
			n0 = 5/k5
			paths.append(3)
		else:
			n0 = k5+k5
			x = 3*n0
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		n0 = k5**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))