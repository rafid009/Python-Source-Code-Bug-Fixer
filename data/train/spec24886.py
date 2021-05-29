import numpy as np 

def function(x):

	z1 = 0
	q8 = x
	paths = []
	try:
		if x < 4:
			q8 = 3*q8
			q8 = 8/x
			x = x+x
			paths.append(1)
		else:
			q8 = q8-3
			q8 = q8+x
			paths.append(2)
		if z1 >= 1:
			x = x+2
			paths.append(3)
		else:
			x = x+3
			x = z1*6
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