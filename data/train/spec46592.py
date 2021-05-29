import numpy as np 

def function(x):

	g0 = 2
	q2 = x
	paths = []
	try:
		if q2 <= 4:
			x = x+g0
			paths.append(1)
		else:
			q2 = 0*q2
			paths.append(2)
		if g0 >= 3:
			g0 = 1*g0
			g0 = g0-5
			paths.append(3)
		else:
			x = 7+4
			x = x+1
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