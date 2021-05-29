import numpy as np 

def function(x):

	k6 = 1
	g3 = 4
	paths = []
	try:
		if g3 < 9:
			g3 = k6-8
			g3 = g3+5
			paths.append(1)
		else:
			g3 = x-4
			x = x+7
			x = x/5
			paths.append(2)
		if g3 > 0:
			g3 = g3-4
			g3 = g3-8
			g3 = 5-g3
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))