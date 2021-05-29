import numpy as np 

def function(x):

	r9 = x
	g5 = x
	x = 6
	paths = []
	try:
		if x < 4:
			r9 = r9-x
			g5 = 1-4
			paths.append(1)
		else:
			g5 = r9-8
			x = 6+x
			paths.append(2)
		if g5 < 7:
			r9 = g5+3
			x = x+8
			paths.append(3)
		else:
			g5 = g5-r9
			x = x*4
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