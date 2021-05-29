import numpy as np 

def function(x):

	f6 = 2
	q2 = x
	paths = []
	try:
		if x < 0:
			q2 = q2-0
			q2 = q2*f6
			paths.append(1)
		else:
			q2 = 8-x
			x = x/4
			paths.append(2)
		if x > 6:
			f6 = 5+3
			q2 = q2-8
			f6 = 6*f6
			paths.append(3)
		else:
			f6 = f6/q2
			x = x*q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))