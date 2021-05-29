import numpy as np 

def function(x):

	g0 = x
	q9 = x
	paths = []
	try:
		if g0 <= 2:
			g0 = q9/6
			x = x-5
			paths.append(1)
		else:
			x = 5*x
			q9 = q9-q9
			x = 7+x
			paths.append(2)
		if x <= 7:
			x = g0/x
			paths.append(3)
		else:
			q9 = 4-3
			x = x/x
			x = 3/3
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