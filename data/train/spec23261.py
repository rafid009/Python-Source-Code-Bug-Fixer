import numpy as np 

def function(x):

	k1 = 5
	q2 = 4
	x = 5
	paths = []
	try:
		if x <= 9:
			k1 = k1-9
			paths.append(1)
		else:
			x = x/q2
			q2 = q2*3
			q2 = 0-q2
			paths.append(2)
		if x <= 0:
			q2 = 0/x
			x = x/k1
			paths.append(3)
		else:
			k1 = k1*4
			q2 = k1*q2
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		q2 = k1**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))