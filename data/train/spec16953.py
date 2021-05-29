import numpy as np 

def function(x):

	s4 = x
	g9 = x
	paths = []
	try:
		if g9 > 4:
			x = g9+2
			paths.append(1)
		else:
			g9 = 8*s4
			paths.append(2)
		if g9 < 0:
			g9 = 9*g9
			g9 = g9/g9
			g9 = g9*x
			paths.append(3)
		else:
			x = x/6
			s4 = 2/s4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))