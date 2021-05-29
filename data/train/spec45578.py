import numpy as np 

def function(x):

	l9 = 0
	g7 = 8
	paths = []
	try:
		if g7 >= 9:
			g7 = g7-9
			g7 = g7*1
			paths.append(1)
		else:
			l9 = 1*1
			l9 = x-6
			x = x*8
			paths.append(2)
		if l9 > 2:
			g7 = g7/x
			x = x+1
			l9 = l9*9
			paths.append(3)
		else:
			g7 = x+g7
			l9 = 4*g7
			l9 = l9+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))