import numpy as np 

def function(x):

	g0 = 8
	q5 = 7
	paths = []
	try:
		if g0 <= 3:
			g0 = g0*9
			paths.append(1)
		else:
			q5 = q5+0
			paths.append(2)
		if g0 > 7:
			g0 = 4-8
			q5 = g0/8
			paths.append(3)
		else:
			q5 = 8/q5
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