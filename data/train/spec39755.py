import numpy as np 

def function(x):

	g9 = x
	l0 = x
	paths = []
	try:
		if l0 <= 8:
			g9 = l0-4
			paths.append(1)
		else:
			l0 = l0/g9
			g9 = 4-g9
			l0 = 6/9
			paths.append(2)
		if x < 4:
			l0 = l0*g9
			x = x*8
			g9 = 5*g9
			paths.append(3)
		else:
			g9 = 8-8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))