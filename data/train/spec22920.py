import numpy as np 

def function(x):

	l9 = x
	g9 = 7
	paths = []
	try:
		if g9 > 6:
			l9 = l9+l9
			g9 = 1*x
			l9 = l9*8
			paths.append(1)
		else:
			x = x-9
			x = 0/x
			paths.append(2)
		if g9 >= 7:
			l9 = l9-4
			x = x+g9
			x = 9+g9
			paths.append(3)
		else:
			l9 = l9/7
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))