import numpy as np 

def function(x):

	n5 = x
	q5 = x
	paths = []
	try:
		if n5 > 3:
			n5 = n5*3
			n5 = q5+n5
			paths.append(1)
		else:
			n5 = n5+8
			paths.append(2)
		if q5 < 9:
			n5 = 5/n5
			paths.append(3)
		else:
			x = x+n5
			n5 = 1*n5
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