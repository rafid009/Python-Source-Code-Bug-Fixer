import numpy as np 

def function(x):

	g7 = x
	q9 = 1
	paths = []
	try:
		if g7 >= 1:
			g7 = g7+2
			x = x*0
			paths.append(1)
		else:
			q9 = 3+3
			paths.append(2)
		if x < 5:
			q9 = q9*g7
			g7 = g7+g7
			g7 = g7*4
			paths.append(3)
		else:
			g7 = 5/g7
			q9 = g7*1
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		q9 = g7**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))