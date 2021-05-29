import numpy as np 

def function(x):

	g5 = x
	q2 = 2
	paths = []
	try:
		if g5 <= 0:
			x = x+4
			paths.append(1)
		else:
			q2 = q2+g5
			paths.append(2)
		if x > 0:
			q2 = 1/q2
			x = x/2
			paths.append(3)
		else:
			q2 = q2/g5
			g5 = 4+3
			g5 = g5+q2
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