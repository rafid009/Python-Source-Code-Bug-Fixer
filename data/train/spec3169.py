import numpy as np 

def function(x):

	n7 = x
	g5 = x
	paths = []
	try:
		if n7 >= 6:
			g5 = g5*5
			g5 = 4*g5
			n7 = 3-n7
			paths.append(1)
		else:
			n7 = n7*n7
			n7 = x+9
			paths.append(2)
		if x >= 5:
			g5 = g5+6
			n7 = n7+7
			paths.append(3)
		else:
			n7 = n7*1
			g5 = g5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))