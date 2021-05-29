import numpy as np 

def function(x):

	q4 = 1
	g8 = 5
	paths = []
	try:
		if x > 7:
			g8 = 4+q4
			g8 = q4+g8
			paths.append(1)
		else:
			q4 = g8-x
			paths.append(2)
		if q4 < 2:
			q4 = q4/x
			g8 = 9-2
			x = 3/x
			paths.append(3)
		else:
			q4 = q4*6
			g8 = 8+x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))