import numpy as np 

def function(x):

	q2 = 5
	b0 = 2
	x = x
	paths = []
	try:
		if x > 1:
			b0 = 3+b0
			paths.append(1)
		else:
			q2 = 1*q2
			paths.append(2)
		if q2 >= 7:
			q2 = b0-3
			q2 = q2+3
			q2 = q2*2
			paths.append(3)
		else:
			q2 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))