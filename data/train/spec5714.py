import numpy as np 

def function(x):

	g1 = x
	w6 = x
	paths = []
	try:
		if x >= 4:
			x = w6/x
			paths.append(1)
		else:
			x = x+w6
			x = w6/x
			paths.append(2)
		if x <= 5:
			x = x/5
			paths.append(3)
		else:
			g1 = 0/7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))