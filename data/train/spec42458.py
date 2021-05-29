import numpy as np 

def function(x):

	w6 = x
	g2 = 6
	paths = []
	try:
		if w6 < 1:
			g2 = w6*g2
			paths.append(1)
		else:
			g2 = g2/3
			w6 = w6+w6
			paths.append(2)
		if w6 < 4:
			g2 = 2/g2
			paths.append(3)
		else:
			x = g2+7
			w6 = g2-9
			x = x-8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		g2 = w6**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))