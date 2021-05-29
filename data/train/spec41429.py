import numpy as np 

def function(x):

	q8 = x
	n5 = 5
	paths = []
	try:
		if n5 < 5:
			q8 = x/2
			x = 7+4
			n5 = n5*n5
			paths.append(1)
		else:
			n5 = n5*n5
			x = 1/x
			paths.append(2)
		if n5 >= 1:
			n5 = x+3
			paths.append(3)
		else:
			x = x*2
			x = x*n5
			x = 4*q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))