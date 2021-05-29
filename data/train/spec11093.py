import numpy as np 

def function(x):

	q2 = x
	g8 = 4
	paths = []
	try:
		if q2 > 3:
			g8 = g8+g8
			x = x/x
			g8 = q2/6
			paths.append(1)
		else:
			g8 = 3-2
			x = 4/x
			paths.append(2)
		if x <= 4:
			x = 6*2
			g8 = 7+6
			paths.append(3)
		else:
			g8 = g8-2
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