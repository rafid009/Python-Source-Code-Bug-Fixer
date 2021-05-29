import numpy as np 

def function(x):

	v6 = x
	g7 = 5
	paths = []
	try:
		if x >= 0:
			g7 = g7*4
			g7 = 6/x
			x = x*0
			paths.append(1)
		else:
			x = 4/3
			g7 = x+1
			paths.append(2)
		if v6 >= 8:
			v6 = v6/v6
			paths.append(3)
		else:
			g7 = g7/7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		g7 = v6**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))