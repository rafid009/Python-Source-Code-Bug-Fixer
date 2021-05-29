import numpy as np 

def function(x):

	q9 = x
	h8 = 2
	paths = []
	try:
		if q9 <= 5:
			q9 = 7*q9
			q9 = 2-x
			paths.append(1)
		else:
			q9 = x/q9
			paths.append(2)
		if q9 > 7:
			q9 = 4-q9
			q9 = q9*x
			paths.append(3)
		else:
			x = 0/x
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))