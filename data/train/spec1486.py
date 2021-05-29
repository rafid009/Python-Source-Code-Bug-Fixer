import numpy as np 

def function(x):

	g3 = x
	l5 = 7
	paths = []
	try:
		if l5 <= 1:
			x = g3+4
			x = x+3
			paths.append(1)
		else:
			g3 = 0-g3
			x = x*2
			paths.append(2)
		if g3 >= 4:
			g3 = g3/2
			x = x/8
			x = x+x
			paths.append(3)
		else:
			l5 = 1*7
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))