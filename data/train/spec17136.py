import numpy as np 

def function(x):

	l9 = 2
	g7 = x
	paths = []
	try:
		if x > 9:
			g7 = x*g7
			g7 = 9/9
			paths.append(1)
		else:
			l9 = l9+1
			paths.append(2)
		if x < 5:
			g7 = 4+x
			g7 = g7*3
			paths.append(3)
		else:
			l9 = l9+2
			l9 = l9+3
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		l9 = g7**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))