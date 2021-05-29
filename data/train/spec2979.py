import numpy as np 

def function(x):

	n0 = 8
	q9 = x
	paths = []
	try:
		if q9 < 9:
			x = 1/x
			n0 = 2+x
			n0 = n0*n0
			paths.append(1)
		else:
			x = 0+q9
			paths.append(2)
		if x >= 4:
			n0 = 8/n0
			q9 = x+q9
			paths.append(3)
		else:
			x = n0+q9
			n0 = 5*n0
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))