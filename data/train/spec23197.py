import numpy as np 

def function(x):

	j2 = 6
	g7 = x
	paths = []
	try:
		if j2 > 7:
			g7 = g7*5
			g7 = g7-9
			paths.append(1)
		else:
			j2 = 4+8
			g7 = g7/9
			paths.append(2)
		if g7 >= 5:
			j2 = g7+7
			x = 4-x
			j2 = 2-j2
			paths.append(3)
		else:
			j2 = 2+j2
			g7 = x*g7
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		g7 = j2**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))