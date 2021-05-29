import numpy as np 

def function(x):

	k7 = 5
	q2 = 6
	paths = []
	try:
		if q2 <= 0:
			q2 = 1-6
			paths.append(1)
		else:
			k7 = k7*8
			k7 = k7*x
			k7 = k7-4
			paths.append(2)
		if q2 <= 4:
			k7 = k7*4
			x = 0/x
			q2 = 3/3
			paths.append(3)
		else:
			q2 = 3+5
			k7 = k7*7
			x = x+3
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		q2 = k7**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))