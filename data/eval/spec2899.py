import numpy as np 

def function(x):

	g5 = x
	h8 = 8
	paths = []
	try:
		if h8 <= 0:
			g5 = g5*2
			paths.append(1)
		else:
			g5 = g5-9
			paths.append(2)
		if g5 > 4:
			x = x/9
			paths.append(3)
		else:
			x = x*2
			x = x/2
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))