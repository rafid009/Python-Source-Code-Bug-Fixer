import numpy as np 

def function(x):

	g5 = x
	q0 = x
	paths = []
	try:
		if q0 >= 2:
			q0 = q0*x
			paths.append(1)
		else:
			q0 = q0-x
			q0 = q0+q0
			paths.append(2)
		if g5 > 6:
			x = 3*7
			paths.append(3)
		else:
			g5 = 6+g5
			x = 0+g5
			x = q0/x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		q0 = g5**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))