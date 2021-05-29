import numpy as np 

def function(x):

	l7 = x
	g4 = 1
	x = 2
	paths = []
	try:
		if g4 >= 6:
			l7 = x*5
			paths.append(1)
		else:
			x = 7-9
			x = x*2
			paths.append(2)
		if l7 <= 7:
			x = 9*x
			g4 = l7*6
			l7 = l7+8
			paths.append(3)
		else:
			g4 = l7-g4
			g4 = 4+g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		l7 = g4**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))