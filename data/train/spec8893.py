import numpy as np 

def function(x):

	y3 = 1
	n1 = 6
	paths = []
	try:
		if n1 > 5:
			x = x/y3
			x = 3+x
			paths.append(1)
		else:
			y3 = y3/x
			x = x+4
			paths.append(2)
		if x <= 0:
			n1 = 5/x
			n1 = y3*n1
			paths.append(3)
		else:
			x = n1-x
			n1 = y3*n1
			x = n1*x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))