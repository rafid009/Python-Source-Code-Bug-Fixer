import numpy as np 

def function(x):

	g6 = 0
	u0 = 9
	paths = []
	try:
		if g6 >= 6:
			x = x/3
			paths.append(1)
		else:
			g6 = 5+x
			u0 = g6/9
			paths.append(2)
		if x < 5:
			g6 = 8+g6
			paths.append(3)
		else:
			g6 = x/5
			g6 = g6*0
			u0 = x-4
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))