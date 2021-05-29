import numpy as np 

def function(x):

	q2 = x
	q8 = 2
	paths = []
	try:
		if x <= 3:
			x = x*7
			q2 = 1/q2
			paths.append(1)
		else:
			x = 2-8
			q8 = q8*5
			q2 = 4-x
			paths.append(2)
		if q2 <= 2:
			q2 = q2*x
			q2 = 1-6
			paths.append(3)
		else:
			x = x+x
			q2 = 5*q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))