import numpy as np 

def function(x):

	g6 = x
	o6 = 0
	paths = []
	try:
		if g6 < 4:
			x = g6-2
			g6 = x-g6
			o6 = o6-5
			paths.append(1)
		else:
			g6 = g6+4
			o6 = o6-1
			o6 = 3+0
			paths.append(2)
		if o6 > 5:
			x = x-5
			paths.append(3)
		else:
			x = 6+7
			o6 = o6-5
			x = 5-g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))