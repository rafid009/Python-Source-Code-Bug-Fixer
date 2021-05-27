import numpy as np 

def function(x):

	q2 = 2
	g5 = x
	paths = []
	try:
		if x >= 3:
			x = 4*x
			x = g5-9
			x = 0*5
			paths.append(1)
		else:
			x = x/7
			q2 = q2/g5
			q2 = 1-x
			paths.append(2)
		if x < 2:
			g5 = g5-2
			g5 = 5-q2
			x = 7-x
			paths.append(3)
		else:
			g5 = g5+6
			x = x-q2
			g5 = g5/6
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		q2 = g5**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))