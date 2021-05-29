import numpy as np 

def function(x):

	q4 = x
	a0 = 9
	x = x
	paths = []
	try:
		if a0 <= 6:
			a0 = 1-a0
			a0 = a0+3
			paths.append(1)
		else:
			a0 = a0*7
			x = 0-x
			q4 = 2*q4
			paths.append(2)
		if x >= 8:
			a0 = a0+x
			paths.append(3)
		else:
			q4 = q4/x
			q4 = q4*9
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))