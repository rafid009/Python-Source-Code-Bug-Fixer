import numpy as np 

def function(x):

	q3 = 7
	n5 = 3
	x = x
	paths = []
	try:
		if x <= 6:
			n5 = 1-n5
			x = x*n5
			paths.append(1)
		else:
			q3 = q3-q3
			n5 = n5*6
			paths.append(2)
		if x <= 4:
			n5 = 6/n5
			q3 = n5*2
			paths.append(3)
		else:
			q3 = q3+x
			q3 = q3+8
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))