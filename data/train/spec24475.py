import numpy as np 

def function(x):

	b2 = x
	q7 = x
	paths = []
	try:
		if q7 <= 0:
			q7 = q7/6
			q7 = b2/q7
			paths.append(1)
		else:
			x = x+b2
			b2 = 5-b2
			paths.append(2)
		if q7 <= 0:
			q7 = q7-b2
			b2 = 1+5
			paths.append(3)
		else:
			x = 6/4
			q7 = 8*q7
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))