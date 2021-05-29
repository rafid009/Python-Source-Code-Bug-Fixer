import numpy as np 

def function(x):

	t5 = x
	g6 = 5
	x = x
	paths = []
	try:
		if g6 <= 0:
			g6 = t5*7
			t5 = t5/2
			paths.append(1)
		else:
			x = 6+x
			g6 = 4+g6
			paths.append(2)
		if t5 > 2:
			g6 = g6/4
			paths.append(3)
		else:
			g6 = g6*3
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		g6 = t5**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))