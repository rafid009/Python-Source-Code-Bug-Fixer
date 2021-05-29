import numpy as np 

def function(x):

	q5 = 8
	g2 = 1
	paths = []
	try:
		if x >= 1:
			x = 0+6
			g2 = g2/4
			paths.append(1)
		else:
			q5 = 2*8
			g2 = 8*9
			q5 = q5*q5
			paths.append(2)
		if g2 < 2:
			q5 = q5/6
			q5 = 0-q5
			paths.append(3)
		else:
			g2 = 3*3
			q5 = 2-q5
			x = x*x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))