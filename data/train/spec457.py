import numpy as np 

def function(x):

	q5 = 7
	n0 = 3
	paths = []
	try:
		if n0 < 9:
			n0 = n0+x
			paths.append(1)
		else:
			n0 = 4*7
			q5 = 1-5
			paths.append(2)
		if n0 < 2:
			n0 = n0/x
			q5 = 2+q5
			paths.append(3)
		else:
			n0 = 7+9
			n0 = 4*n0
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