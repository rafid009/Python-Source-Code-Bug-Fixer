import numpy as np 

def function(x):

	g7 = x
	l3 = x
	paths = []
	try:
		if l3 >= 9:
			x = x-x
			paths.append(1)
		else:
			l3 = 7+5
			l3 = l3*g7
			l3 = x/6
			paths.append(2)
		if x > 4:
			g7 = 1/g7
			g7 = 4-g7
			paths.append(3)
		else:
			g7 = g7-7
			l3 = l3*g7
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))