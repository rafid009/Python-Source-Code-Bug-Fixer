import numpy as np 

def function(x):

	q1 = x
	k6 = 4
	paths = []
	try:
		if q1 <= 3:
			k6 = 9+k6
			q1 = q1*q1
			paths.append(1)
		else:
			k6 = k6+8
			q1 = 4*5
			paths.append(2)
		if x >= 0:
			x = x*5
			paths.append(3)
		else:
			k6 = k6+x
			q1 = 8-q1
			k6 = 5/k6
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