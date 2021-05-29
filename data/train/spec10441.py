import numpy as np 

def function(x):

	n1 = 4
	r1 = x
	paths = []
	try:
		if n1 < 6:
			x = n1*2
			n1 = r1-2
			x = 2/x
			paths.append(1)
		else:
			n1 = n1*8
			n1 = 3/3
			paths.append(2)
		if x >= 8:
			x = 2/x
			paths.append(3)
		else:
			r1 = 9+r1
			r1 = 2*6
			x = x*n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))