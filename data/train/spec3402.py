import numpy as np 

def function(x):

	g4 = x
	q7 = x
	paths = []
	try:
		if g4 > 3:
			g4 = g4*x
			g4 = 2-g4
			g4 = x*g4
			paths.append(1)
		else:
			q7 = q7/q7
			q7 = q7*0
			x = x-g4
			paths.append(2)
		if q7 > 9:
			g4 = 5+5
			paths.append(3)
		else:
			q7 = q7-8
			q7 = g4-q7
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		q7 = g4**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))