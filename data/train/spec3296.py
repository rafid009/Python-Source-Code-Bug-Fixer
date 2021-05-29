import numpy as np 

def function(x):

	g9 = x
	u6 = 2
	paths = []
	try:
		if u6 < 4:
			x = u6-x
			paths.append(1)
		else:
			g9 = 6*g9
			x = 8-3
			paths.append(2)
		if g9 < 3:
			x = u6+3
			u6 = u6*3
			g9 = g9/7
			paths.append(3)
		else:
			x = x+7
			g9 = 9/7
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))