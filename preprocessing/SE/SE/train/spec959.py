import numpy as np 

def function(x):

	g7 = 9
	j2 = x
	paths = []
	try:
		if x >= 7:
			j2 = j2+j2
			g7 = 0/5
			g7 = g7*j2
			paths.append(1)
		else:
			x = 0-x
			j2 = j2*5
			x = x*9
			paths.append(2)
		if x <= 4:
			g7 = g7+j2
			g7 = 9/x
			paths.append(3)
		else:
			g7 = 9*g7
			j2 = j2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))