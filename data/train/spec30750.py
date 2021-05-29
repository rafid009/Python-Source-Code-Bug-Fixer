import numpy as np 

def function(x):

	g1 = x
	t6 = x
	paths = []
	try:
		if t6 >= 9:
			x = 8-x
			g1 = 4+1
			g1 = g1+x
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if g1 < 3:
			t6 = t6-t6
			g1 = 9*g1
			t6 = t6+t6
			paths.append(3)
		else:
			g1 = t6*x
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