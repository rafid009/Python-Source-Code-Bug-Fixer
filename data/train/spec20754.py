import numpy as np 

def function(x):

	q4 = 1
	p6 = 5
	paths = []
	try:
		if q4 <= 9:
			x = p6-x
			paths.append(1)
		else:
			p6 = 1+1
			paths.append(2)
		if x <= 7:
			p6 = 0-q4
			paths.append(3)
		else:
			q4 = q4*3
			q4 = 0*q4
			x = x/x
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