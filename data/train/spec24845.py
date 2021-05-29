import numpy as np 

def function(x):

	g1 = 4
	v9 = 6
	paths = []
	try:
		if x <= 5:
			x = x*g1
			g1 = g1+x
			paths.append(1)
		else:
			g1 = g1*0
			g1 = 5*1
			paths.append(2)
		if g1 > 2:
			x = 9-x
			g1 = g1-4
			paths.append(3)
		else:
			x = x*9
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