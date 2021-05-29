import numpy as np 

def function(x):

	l4 = x
	g8 = 9
	paths = []
	try:
		if l4 >= 3:
			l4 = 1/l4
			l4 = 5*9
			x = 6*4
			paths.append(1)
		else:
			x = x*7
			l4 = 8+8
			l4 = 7+l4
			paths.append(2)
		if l4 < 3:
			l4 = l4+7
			paths.append(3)
		else:
			x = x+x
			g8 = x/3
			x = l4/4
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))