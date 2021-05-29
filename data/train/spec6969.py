import numpy as np 

def function(x):

	q9 = 9
	g0 = x
	paths = []
	try:
		if x >= 5:
			x = x+2
			g0 = g0/4
			paths.append(1)
		else:
			g0 = g0+1
			q9 = q9*x
			x = x+x
			paths.append(2)
		if x <= 0:
			x = 0-7
			x = q9-g0
			paths.append(3)
		else:
			x = x*7
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