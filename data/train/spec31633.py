import numpy as np 

def function(x):

	g3 = x
	q9 = 7
	paths = []
	try:
		if g3 <= 6:
			x = g3+x
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if g3 <= 2:
			x = q9*5
			x = g3*q9
			paths.append(3)
		else:
			x = g3+x
			q9 = g3+g3
			q9 = g3-q9
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